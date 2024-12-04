from django.db import models


class Merchant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MerchantItem(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name="merchants")
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.item.name} for {self.price} gold"
