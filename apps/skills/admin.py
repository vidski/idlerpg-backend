from django.contrib import admin

from apps.skills.models import Skill, SkillProgress

# Register your models here.
admin.site.register(Skill)
admin.site.register(SkillProgress)
