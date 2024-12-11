from django.contrib.auth.models import AbstractUser

from apps.currencies.models import UserCurrencies
from apps.equipment.models import UserLoadout


class User(AbstractUser):
    # created_at = models.DateTimeField("created at", auto_now_add=True)
    # modified_at = models.DateTimeField("modified at", auto_now=True)

    def __str__(self):
        return self.email if self.email else self.username

    def save(self, *args, **kwargs):
        new = False
        if self.pk is None:
            new = True
        super().save(*args, **kwargs)
        if new:
            UserCurrencies.objects.create(user=self)
            UserLoadout.objects.create(user=self)
