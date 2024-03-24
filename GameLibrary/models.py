from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_admin_creation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": "This game already exists."},
        help_text="Enter the name of the game",
        blank=False,
        null=False,
    )
    creator = models.CharField(
        max_length=200,
        help_text="Enter the creator of the game",
        blank=False,
        null=False,
    )
    platforms = models.CharField(
        max_length=50,
        help_text="Enter the platforms the game is available on",
    )
    release_date = models.DateField(
        help_text="Enter the release date of the game",
    )
    is_free = models.BooleanField(
        help_text="Is the game free?",
    )
    num_players = models.IntegerField(
        help_text="Enter the number of players",
    )
    global_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        help_text="Enter the global rating of the game",
    )
    is_multiplayer = models.BooleanField(
        help_text="Is the game multiplayer?",
    )
    genere = models.CharField(
        max_length=50,
        help_text="Enter the genere of the game",
    )
    description = models.TextField(
        help_text="Enter the description of the game",
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="covers/", null=True, blank=True)

    def __str__(self):
        return self.name


class UserGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    personal_rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True
    )
    playing_state = models.CharField(max_length=50)

    class Meta:
        unique_together = ("user", "game")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment by {} on {}".format(self.user.username, self.post.title)