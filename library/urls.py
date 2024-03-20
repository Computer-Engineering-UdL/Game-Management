from django.urls import path
from library.views import GameListView

urlpatterns = [
    path("games/", GameListView.as_view(), name="game-list"),
]
