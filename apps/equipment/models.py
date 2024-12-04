from django.conf import settings
from django.db import models


class UserLoadout(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='loadout')
    weapon = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_weapon'
    )
    armor = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_armor'
    )
    helmet = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_helmet'
    )
    boots = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_boots'
    )
    ring_left = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_ring_left'
    )
    ring_right = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_ring_right'
    )
    accessory = models.OneToOneField(
        'inventory.InventoryItem', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipped_as_accessory'
    )

    def __str__(self):
        return f'{self.user.username}s loadout'

