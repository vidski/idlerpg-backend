from django.contrib import admin

from apps.equipment.models import EquippedItem

@admin.register(EquippedItem)
class EquippedItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'weapon', 'armor', 'helmet', 'boots', 'ring_left', 'ring_right', 'accessory']
