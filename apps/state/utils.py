from apps.authentication.models import User
from apps.state.serializers import UserStateSerializer


def get_user_state(user_id):
    user = User.objects.select_related(
        'action',
        'loadout'
    ).prefetch_related(
        'inventory',
        'skill_progress'
    ).get(id=user_id)

    return UserStateSerializer(user).data
