from django.contrib import admin, messages
from django.db.models import F

from apps.inventory.models import InventoryItem
from apps.logs.models import InventoryLog


@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'change', 'reason', 'timestamp']

    actions = ['rollback_changes']

    def rollback_changes(self, request, queryset):
        successful_rollbacks = 0
        failed_rollbacks = 0

        for log in queryset:
            try:
                # Find the corresponding inventory item
                inventory_item = InventoryItem.objects.get(user=log.user, item=log.item)

                # Rollback the change
                new_quantity = inventory_item.quantity - log.change

                if new_quantity < 0:
                    # Ensure we don't rollback to negative inventory
                    failed_rollbacks += 1
                    self.message_user(
                        request,
                        f"Cannot rollback log for {log.item.name} (user: {log.user.username}) "
                        f"because it would result in negative inventory.",
                        level=messages.WARNING
                    )
                    continue

                inventory_item.quantity = F('quantity') - log.change
                inventory_item.save()

                # Log the rollback as a new inventory log
                InventoryLog.objects.create(
                    user=log.user,
                    item=log.item,
                    change=-log.change,  # Reverse the original change
                    reason=f"Rollback of log {log.id}"
                )
                successful_rollbacks += 1
            except InventoryItem.DoesNotExist:
                # If the inventory item doesn't exist, skip the rollback
                failed_rollbacks += 1
                self.message_user(
                    request,
                    f"Cannot rollback log for {log.item.name} (user: {log.user.username}) "
                    f"because the inventory item does not exist.",
                    level=messages.WARNING
                )

        # Summary message
        if successful_rollbacks > 0:
            self.message_user(
                request,
                f"Successfully rolled back {successful_rollbacks} inventory logs.",
                level=messages.SUCCESS
            )
        if failed_rollbacks > 0:
            self.message_user(
                request,
                f"Failed to rollback {failed_rollbacks} inventory logs.",
                level=messages.WARNING
            )

    rollback_changes.short_description = "Rollback selected inventory logs"
