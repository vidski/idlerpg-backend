from rest_framework import serializers

from apps.items.serializers import ItemSerializer
from .models import InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['item', 'quantity', 'durability', 'custom_name']


class MinimalInventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        fields = ['id', 'item_id', 'quantity']