from django.contrib import admin
from .models import GameProgress, GameLevel, UserGameResult

admin.site.register(GameProgress)
admin.site.register(GameLevel)
admin.site.register(UserGameResult)
