from rest_framework import serializers

from apps.currencies.models import UserCurrencies


class UserCurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCurrencies
        fields = [
            'gold',
        ]
