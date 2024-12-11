from rest_framework import viewsets, permissions
from rest_framework.response import Response

from apps.items.models import Item
from apps.items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Transform the response data
        data = {str(item['id']): {**item} for item in serializer.data}
        return Response(data)
