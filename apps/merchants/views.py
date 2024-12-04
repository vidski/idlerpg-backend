from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.currencies.models import UserCurrencies
from apps.inventory.models import InventoryItem
from apps.merchants.models import Merchant, MerchantItem


class BuyItemView(APIView):
    http_method_names = ['post']

    def post(self, request):
        item_id = request.data.get('id')
        quantity = request.data.get('quantity')

        if not item_id or not quantity:
            return Response({"error": "Item ID and quantity are required"}, status=400)

        try:
            merchant = Merchant.objects.prefetch_related('items').get(id=1)
            merchant_item = merchant.items.get(item_id=item_id)
        except Merchant.DoesNotExist:
            return Response({"error": "Merchant not found"}, status=404)
        except MerchantItem.DoesNotExist:
            return Response({"error": "Item not found in merchant's inventory"}, status=404)

        with transaction.atomic():
            # Calculate total cost
            total_cost = merchant_item.price * quantity

            # Check if user has enough gold
            user_currencies = UserCurrencies.objects.select_for_update().get(user_id=request.user.id)
            if user_currencies.gold < total_cost:
                return Response({"error": "Not enough gold to purchase the item"}, status=400)

            # Deduct gold from the user's account
            user_currencies.gold -= total_cost
            user_currencies.save(update_fields=['gold'])

            # Add item to user's inventory
            inventory_item, created = InventoryItem.objects.get_or_create(
                item_id=item_id,
                user_id=request.user.id,
                defaults={'quantity': 0}
            )
            inventory_item.quantity += quantity
            inventory_item.save(update_fields=['quantity'])

        return Response({"message": "Item purchased successfully"}, status=200)
