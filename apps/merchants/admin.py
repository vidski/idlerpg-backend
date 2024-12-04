from django.contrib import admin

from apps.merchants.models import MerchantItem, Merchant

admin.site.register(MerchantItem)
admin.site.register(Merchant)
