from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.actions.models import Action, UserAction
from apps.state.utils import get_user_state


class StartActionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        skill_id = request.data.get('skill_id')
        action_id = request.data.get('action_id')

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
        response_data = get_user_state(request.user.id)
        return Response(response_data)


class StopActionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_action = get_object_or_404(UserAction, user=request.user)

        if not user_action:
            return Response({"error": "No active action found"}, status=400)

        user_action.complete()

        # Use state serializer to return full user state
        response_data = get_user_state(request.user.id)
        return Response(response_data)
