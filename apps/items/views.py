from rest_framework import viewsets, permissions

from apps.items.models import Item
from apps.items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
