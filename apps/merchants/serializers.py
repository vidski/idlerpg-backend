from rest_framework import serializers

from apps.merchants.models import Merchant, MerchantItem


class MerchantItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantItem
        fields = ['item_id', 'price']


class MerchantSerializer(serializers.ModelSerializer):
    items = MerchantItemSerializer(many=True, read_only=True)

    class Meta:
        model = Merchant
        fields = '__all__'
