from rest_framework import views
from rest_framework.response import Response

from apps.inventory.models import InventoryItem
from .models import EquippedItem
from .serializers import EquippedItemSerializer


class EquippedItemView(views.APIView):
    def get(self, request, *args, **kwargs):
        equipped_items, created = EquippedItem.objects.get_or_create(user=request.user)
        serializer = EquippedItemSerializer(equipped_items)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        slot = request.data.get('slot')
        inventory_item_id = request.data.get('inventory_item_id')

        equipped_items, created = EquippedItem.objects.get_or_create(user=request.user)
        inventory_item = InventoryItem.objects.get(id=inventory_item_id, user=request.user)

        setattr(equipped_items, slot, inventory_item)
        equipped_items.save()

        return Response({"message": f"Item equipped in {slot} slot."})
