from django.db import models


class Enemy(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    speed = models.FloatField()
    level = models.IntegerField()
