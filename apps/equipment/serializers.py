from rest_framework import serializers
from .models import EquippedItem
from apps.inventory.serializers import InventoryItemSerializer

class EquippedItemSerializer(serializers.ModelSerializer):
    weapon = InventoryItemSerializer(read_only=True)
    armor = InventoryItemSerializer(read_only=True)
    helmet = InventoryItemSerializer(read_only=True)
    boots = InventoryItemSerializer(read_only=True)
    ring_left = InventoryItemSerializer(read_only=True)
    ring_right = InventoryItemSerializer(read_only=True)
    accessory = InventoryItemSerializer(read_only=True)

    class Meta:
        model = EquippedItem
        fields = ['user', 'weapon', 'armor', 'helmet', 'boots', 'ring_left', 'ring_right', 'accessory']