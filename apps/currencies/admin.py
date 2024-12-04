from django.contrib import admin

from apps.currencies.models import UserCurrencies


@admin.register(UserCurrencies)
class UserCurrenciesAdmin(admin.ModelAdmin):
    list_display = ['user', 'gold']
