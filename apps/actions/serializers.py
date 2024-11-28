from rest_framework import serializers
from .models import UserAction

class ActionStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = ['skill', 'action', 'seed', 'start_date']
