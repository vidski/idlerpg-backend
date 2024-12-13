# Create your models here.
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    item_type = models.CharField(max_length=50, choices=[
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('helmet', 'Helmet'),
        ('boots', 'Boots'),
        ('ring', 'Ring'),
        ('accessory', 'Accessory'),
        ('misc', 'Miscellaneous')
    ])
    sell_price = models.PositiveIntegerField(default=0)
    image_name = models.CharField(max_length=100, default='missing.png')
    rarity = models.CharField(max_length=50, choices=[
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary')
    ])
    equippable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

