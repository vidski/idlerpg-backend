from django.db import transaction
from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InventoryItem
from .serializers import InventoryItemSerializer
from ..currencies.models import UserCurrencies


class InventoryItemListView(generics.ListAPIView):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)


class SellItemView(APIView):
    http_method_names = ['post']

    def post(self, request):
        item_id = request.data.get('id')
        quantity = request.data.get('quantity')
        with transaction.atomic():
            inventory_item = InventoryItem.objects.select_related('item').get(id=item_id, user_id=request.user.id)
            inventory_item.quantity -= quantity
            if inventory_item.quantity < 0:
                return Response({"error": "Not enough items to sell"}, status=400)

            if inventory_item.quantity == 0:
                inventory_item.delete()
            else:
                inventory_item.save(update_fields=['quantity'])

            UserCurrencies.objects.update(user_id=request.user.id, gold=F('gold') + inventory_item.item.sell_price * quantity)
        return Response({"message": "Item sold successfully"})
