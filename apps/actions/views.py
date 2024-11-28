from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.actions.models import Action, UserAction
from apps.inventory.models import InventoryItem
from apps.items.utils import calculate_loot
from apps.logs.models import InventoryLog
from apps.skills.models import SkillProgress
from apps.state.serializers import UserStateSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_action(request):
    skill_id = request.data.get('skillId')
    action_id = request.data.get('actionId')

    action = get_object_or_404(Action, id=action_id, skill_id=skill_id)

    # Generate a seed based on current time and user
    current_time = timezone.now().isoformat()
    seed = f"{current_time}{request.user.id}{action_id}"

    # Check if user already has an active action
    has_user_action = UserAction.objects.filter(user=request.user).exists()
    if has_user_action:
        return Response({"error": "User already has an active action"}, status=400)

    # Create or update user action
    UserAction.objects.create(
        user=request.user,
        skill_id=skill_id,
        action=action,
        seed=seed,
        start_date=current_time
    )

    # Use state serializer to return full user state
    serializer = UserStateSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_action(request):
    try:
        user_action = UserAction.objects.select_related('action', 'skill').get(user=request.user)

        # Calculate duration
        start_time = user_action.start_date
        end_time = timezone.now()
        duration = (end_time - start_time).total_seconds()

        # Calculate loot using existing utility
        loot = calculate_loot(user_action.seed, int(duration), user_action.action)

        # Calculate experience based on completed actions
        actions_completed = duration // user_action.action.duration
        total_exp = actions_completed * user_action.action.experience

        # Update skill progress
        skill_progress, _ = SkillProgress.objects.get_or_create(
            user=request.user,
            skill=user_action.skill
        )
        skill_progress.experience += total_exp
        skill_progress.save()

        # Update inventory
        inventory_items = []
        inventory_logs = []

        for item_id, item_data in loot.items():
            print(item_id, item_data)
            inventory_item, created = InventoryItem.objects.get_or_create(
                user=request.user,
                item_id=item_id,
                defaults={'quantity': 0}
            )
            inventory_item.quantity += item_data['quantity']
            inventory_items.append(inventory_item)

            inventory_logs.append(InventoryLog(
                user=request.user,
                item_id=item_id,
                change=item_data['quantity'],
                reason='action_reward'
            ))

        # Bulk update inventory items
        InventoryItem.objects.bulk_update(inventory_items, ['quantity'])

        # Bulk create inventory logs
        InventoryLog.objects.bulk_create(inventory_logs)

        user_action.delete()

        # Return updated user state
        serializer = UserStateSerializer(request.user)
        return Response(serializer.data)

    except UserAction.DoesNotExist:
        return Response({"error": "No active action found"}, status=400)
