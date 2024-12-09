from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.state.utils import get_user_state


class UserStateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response_data = get_user_state(request.user.id)
        return Response(response_data)
