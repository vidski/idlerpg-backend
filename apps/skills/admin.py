from django.contrib import admin

from apps.skills.models import Skill, SkillProgress


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(SkillProgress)
class SkillProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'skill', 'experience', 'level', 'experience_to_next_level', 'experience_for_current_level']
