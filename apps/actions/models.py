from django.db import models

from apps.inventory.models import InventoryItem
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

    experience = models.FloatField()
    duration = models.FloatField()

    item_requirements = models.ManyToManyField('items.Item', through=ActionRequirement, blank=True, related_name='item_requirements')
    item_rewards = models.ManyToManyField('items.Item', through=ActionReward, blank=True, related_name='item_rewards')


class UserAction(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE, related_name='action')
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    action = models.ForeignKey('actions.Action', on_delete=models.CASCADE)
    seed = models.CharField(max_length=100)
    start_date = models.DateTimeField()
