from rest_framework import serializers

from apps.actions.models import UserAction
from apps.authentication.models import User
from apps.equipment.serializers import EquippedItemSerializer
from apps.inventory.serializers import InventoryItemSerializer
from apps.skills.serializers import SkillProgressSerializer
from apps.actions.serializers import ActionStateSerializer


class UserStateSerializer(serializers.ModelSerializer):
    inventory = InventoryItemSerializer(many=True, read_only=True)
    equipment = EquippedItemSerializer(read_only=True, source='loadout')
    skill_progress = SkillProgressSerializer(many=True, read_only=True)
    action = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'inventory',
            'equipment',
            'skill_progress',
            'action'
        ]

    def get_action(self, obj):
        try:
            user_action = obj.action
            if user_action:
                return {
                    'startDate': user_action.start_date,
                    'seed': user_action.seed,
                    'skillId': str(user_action.skill.id),
                    'actionId': str(user_action.action.id),
                }
        except UserAction.DoesNotExist:
            return None
