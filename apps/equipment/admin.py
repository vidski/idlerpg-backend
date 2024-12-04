from django.contrib import admin

from apps.equipment.models import UserLoadout

@admin.register(UserLoadout)
class UserLoadoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'weapon', 'armor', 'helmet', 'boots', 'ring_left', 'ring_right', 'accessory']
