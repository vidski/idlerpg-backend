from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class InventoryItemListView(generics.ListAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)


class SellItemView(APIView):
    http_method_names = ['post']

    def post(self, request):
        item_id = request.data.get('id')
        quantity = request.data.get('quantity')
        item = InventoryItem.objects.get(id=item_id, user_id=request.user.id)
        item.quantity -= quantity
        if item.quantity == 0:
            item.delete()
        else:
            item.save()
        return Response({"message": "Item sold successfully"})
