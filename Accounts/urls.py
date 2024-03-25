from django.urls import path
from Accounts import views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
]