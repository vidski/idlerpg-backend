from django.contrib import admin

from apps.items.models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'item_type', 'rarity', 'equippable']
