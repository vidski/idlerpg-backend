from rest_framework import serializers

from apps.items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'item_type', 'sell_price', 'rarity', 'image_name', 'equippable']
