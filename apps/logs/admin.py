from django.contrib import admin

from apps.logs.models import InventoryLog


@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'change', 'reason', 'timestamp']
