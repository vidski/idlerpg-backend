from django.contrib import admin

from apps.actions.models import Action, ActionReward, UserAction, ActionRequirement


# Register your models here.

class ActionRewardInline(admin.TabularInline):
    model = ActionReward
    extra = 0


class ActionRequirementInline(admin.TabularInline):
    model = ActionRequirement
    extra = 0


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill', 'skill_level']
    inlines = [ActionRequirementInline, ActionRewardInline]


@admin.register(UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ['user', 'skill', 'action', 'start_date']
    actions = ['complete_user_action']

    @admin.action(description='Complete selected user actions')
    def complete_user_action(self, request, queryset):
        for user_action in queryset:
            user_action.complete()