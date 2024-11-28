from django.contrib import admin

from apps.achievements.models import Achievement, UserAchievement


# Register your models here.
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'achieved_at']
