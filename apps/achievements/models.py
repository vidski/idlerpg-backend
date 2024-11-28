from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    achievement = models.ForeignKey('achievements.Achievement', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.achievement}'

