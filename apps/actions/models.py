from random import random

from django.db import models
from django.utils import timezone

from apps.inventory.models import InventoryItem
from apps.items.utils import calculate_loot
from apps.logs.models import InventoryLog
from apps.skills.models import SkillProgress


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
        end_date = timezone.now()
        duration = (end_date - self.start_date).total_seconds()

        # Calculate experience
        experience = (duration / self.action.duration) * self.action.experience
        loot = calculate_loot(self.seed, int(duration), self.action, list(ActionReward.objects.filter(action=self.action)))

        # Add loot to inventory and log
        for index, item in loot.items():
            inventory_item, created = InventoryItem.objects.get_or_create(
                user=self.user, item_id=item.get('id'),
                defaults={'quantity': 0}
            )
            inventory_item.quantity += item.get('quantity')
            inventory_item.save()
            InventoryLog.objects.create(
                user=self.user, item_id=item.get('id'), change=item.get('quantity'), reason=f"Action reward from {self.action.name}"
            )

        # Create or update SkillProgress
        skill_progress, created = SkillProgress.objects.get_or_create(
            user=self.user, skill=self.skill,
            defaults={'experience': 0}
        )
        if not created:
            skill_progress.experience += experience
            skill_progress.save()

        # Delete the UserAction
        self.delete()

        return loot
