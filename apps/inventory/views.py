from rest_framework import generics

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class InventoryItemListView(generics.ListAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)
