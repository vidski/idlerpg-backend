from django.contrib import admin

from apps.market.models import MarketListing


@admin.register(MarketListing)
class MarketListingAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'price', 'quantity', 'created_at']
