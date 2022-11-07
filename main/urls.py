from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include  #add include


app_name = "main"   


urlpatterns = [
    path("https://listando.netlify.app/", views.homepage, name="homepage"),
    path("https://listando.netlify.app/register", views.register_request, name="register"),
    path("https://listando.netlify.app/login", views.login_request, name="login"),
    path("https://listando.netlify.app/logout", views.logout_request, name= "logout"),
    path("https://listando.netlify.app/sucesso", views.homepage, name="sucesso")
]
