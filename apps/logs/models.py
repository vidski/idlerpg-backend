from django.conf import settings
from django.db import models


class InventoryLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inventory_logs")
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name="logs")
    change = models.IntegerField()  # Positive for adding items, negative for removing
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        action = "Added" if self.change > 0 else "Removed"
        return f"{action} {abs(self.change)} x {self.item.name} for {self.user.username}"

