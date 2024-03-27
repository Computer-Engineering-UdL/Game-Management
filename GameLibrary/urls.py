from django.urls import path
from GameLibrary import views

urlpatterns = [
    path("games/", views.game_list, name="game-list"),
    path("games/<int:pk>/", views.game_detail, name="game-detail"),
]
