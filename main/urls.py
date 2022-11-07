from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include  #add include


app_name = "main"   


urlpatterns = [
    path("https://listando.herokuapp.com/", views.homepage, name="homepage"),
    path("https://listando.herokuapp.com/register", views.register_request, name="register"),
    path("https://listando.herokuapp.com/login", views.login_request, name="login"),
    path("https://listando.herokuapp.com/logout", views.logout_request, name= "logout"),
    path("https://listando.herokuapp.com/sucesso", views.homepage, name="sucesso")
]
