from django.contrib import admin
from GameLibrary.models import Game, Post, Comment, UserGame

admin.site.register(Game)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserGame)
