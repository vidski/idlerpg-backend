from django.contrib import admin

from apps.actions.models import Action, ActionReward, UserAction

# Register your models here.
admin.site.register(Action)
admin.site.register(ActionReward)
admin.site.register(UserAction)
