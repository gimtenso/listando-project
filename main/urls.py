from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include  #add include


app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("sucesso", views.sucesso, name="sucesso")
]
