from django.contrib import admin

from apps.combat.models import Enemy


# Register your models here.
@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'health', 'attack', 'defense', 'speed']
