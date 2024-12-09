import math

from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class SkillProgress(models.Model):
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='skills')
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.skill}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['skill', 'user'], name='unique_skill_progress')
        ]

    @property
    def level(self):
        base = 100  # Base experience required for level 1
        growth_factor = 1.5  # Exponential growth factor
        level = 1
        exp = self.experience

        while exp >= base * (level ** growth_factor):
            exp -= base * (level ** growth_factor)
            level += 1

        return level

    @property
    def experience_to_next_level(self):
        base = 100
        growth_factor = 1.5
        current_level = self.level
        next_level_exp = base * (current_level ** growth_factor)
        exp_to_next = next_level_exp - (self.experience - self.experience_for_current_level)

        return math.ceil(exp_to_next)

    @property
    def experience_for_current_level(self):
        base = 100
        growth_factor = 1.5
        level = self.level
        exp_for_current = sum(base * (l ** growth_factor) for l in range(1, level))

        return exp_for_current
