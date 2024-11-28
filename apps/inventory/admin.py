from django.contrib import admin

from apps.inventory.models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'quantity']
