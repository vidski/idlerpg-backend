from django.db import models
from django.utils import timezone

from apps.inventory.models import InventoryItem
from apps.logs.models import InventoryLog
from apps.skills.models import SkillProgress
from core.utils import SplitMix64


class ActionTypes(models.TextChoices):
    COMBAT = 'COMBAT', 'COMBAT'
    GATHER = 'GATHER', 'GATHER'
    CRAFT = 'CRAFT', 'CRAFT'


class ActionRequirement(models.Model):
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    action = models.ForeignKey('actions.Action', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    keep_after_action = models.BooleanField(default=False)


class ActionReward(models.Model):
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    action = models.ForeignKey('actions.Action', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    drop_rate = models.FloatField(default=1.0)


class Action(models.Model):
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    skill_level = models.IntegerField()
    action_type = models.CharField(choices=ActionTypes.choices, max_length=10)
    combat = models.ForeignKey('combat.Enemy', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    translations = models.JSONField(default=dict)

    experience = models.FloatField()
    duration = models.FloatField()

    item_requirements = models.ManyToManyField('items.Item', through=ActionRequirement, blank=True, related_name='item_requirements')
    item_rewards = models.ManyToManyField('items.Item', through=ActionReward, blank=True, related_name='item_rewards')

    def __str__(self):
        return self.name


class UserAction(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE, related_name='action')
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    action = models.ForeignKey('actions.Action', on_delete=models.CASCADE)
    seed = models.CharField(max_length=100)
    start_date = models.DateTimeField()

    def complete(self):
        # Calculate duration
        elapsed_time = (timezone.now() - self.start_date).total_seconds()
        action_duration = self.action.duration
        action_count = int(elapsed_time // action_duration)

        if action_count <= 0:
            self.delete()
            return None

        # Aggregate rewards
        action_rewards = ActionReward.objects.filter(action=self.action)
        rng = SplitMix64(int(self.seed))
        total_loot = {}

        for _ in range(action_count):  # Process each cycle independently
            for reward in action_rewards:
                if rng.next_float() <= reward.drop_rate:  # Independent drop chance per action
                    quantity = rng.next_int(1, reward.quantity)
                    total_loot[reward.item_id] = total_loot.get(reward.item_id, 0) + quantity

        # Batch inventory updates
        existing_inventory = InventoryItem.objects.filter(user=self.user, item_id__in=total_loot.keys())
        existing_inventory_map = {item.item_id: item for item in existing_inventory}

        items_to_update = []
        items_to_create = []
        logs = []

        for item_id, quantity in total_loot.items():
            if item_id in existing_inventory_map:
                inventory_item = existing_inventory_map[item_id]
                inventory_item.quantity += quantity
                items_to_update.append(inventory_item)
            else:
                items_to_create.append(
                    InventoryItem(
                        user=self.user,
                        item_id=item_id,
                        quantity=quantity
                    )
                )

            # Create a log entry
            logs.append(
                InventoryLog(
                    user=self.user,
                    item_id=item_id,
                    change=quantity,
                    reason="Mining reward"
                )
            )

        if items_to_update:
            InventoryItem.objects.bulk_update(items_to_update, ['quantity'])
        if items_to_create:
            InventoryItem.objects.bulk_create(items_to_create)
        if logs:
            InventoryLog.objects.bulk_create(logs)

        # Clean up user action
        self.delete()

        # Prepare readable loot for response
        loot_response = [
            {"item": reward.item.name, "quantity": total_loot[reward.item_id]}
            for reward in action_rewards
            if reward.item_id in total_loot
        ]

        return loot_response
