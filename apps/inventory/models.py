from django.db import models


class InventoryItem(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='inventory')
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.PositiveIntegerField(default=1)
    acquired_at = models.DateTimeField(auto_now_add=True)
    durability = models.IntegerField(null=True, blank=True)
    custom_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f'{self.user} - {self.item.name} x{self.quantity}'
