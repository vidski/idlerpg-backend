from apps.authentication.models import User
from apps.state.serializers import UserStateSerializer


def get_user_state(user_id):
    user = User.objects.select_related(
        'action',
        'loadout',
        'currencies'
    ).prefetch_related(
        'inventory',
        'skills',
    ).get(id=user_id)

    return UserStateSerializer(user).data
