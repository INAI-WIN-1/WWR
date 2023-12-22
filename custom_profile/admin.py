from django.contrib import admin

from custom_profile.models import Game, CustomUser

admin.site.register(Game)
admin.site.register(CustomUser)