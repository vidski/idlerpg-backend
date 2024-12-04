from django.db import models


class UserCurrencies(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE, related_name='currencies')
    gold = models.PositiveIntegerField(default=0)
