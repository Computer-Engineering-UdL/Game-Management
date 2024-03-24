from django.shortcuts import render
from django.views.generic import ListView
from GameLibrary.models import Game


class GameListView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "games"
