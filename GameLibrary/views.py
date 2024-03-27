from django.shortcuts import render
from django.views.generic import ListView
from GameLibrary.models import Game


def game_list(request):
    games = Game.objects.all()
    return render(request, "games/game_list.html", {"games": games})


def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, "games/game_detail.html", {"game": game})

