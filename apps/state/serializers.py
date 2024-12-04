from rest_framework import serializers

from apps.actions.models import UserAction
from apps.actions.serializers import ActionStateSerializer
from apps.authentication.models import User
from apps.currencies.serializers import UserCurrenciesSerializer
from apps.equipment.serializers import EquippedItemSerializer
from apps.inventory.serializers import MinimalInventoryItemSerializer
from apps.skills.serializers import SkillProgressSerializer


class UserStateSerializer(serializers.ModelSerializer):
    inventory = MinimalInventoryItemSerializer(many=True, read_only=True)
    equipment = EquippedItemSerializer(read_only=True, source='loadout')
    currencies = UserCurrenciesSerializer(read_only=True)
    skill_progress = SkillProgressSerializer(many=True, read_only=True)
    action = ActionStateSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'is_active',
            'inventory',
            'equipment',
            'currencies',
            'skill_progress',
            'action',
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
