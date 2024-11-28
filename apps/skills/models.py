from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class SkillProgress(models.Model):
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='skill_progress')
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.skill}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['skill', 'user'], name='unique_skill_progress')
        ]
