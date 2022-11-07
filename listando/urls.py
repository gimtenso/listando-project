from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('https://listando.herokuapp.com/admin/', admin.site.urls),
    path('https://listando.herokuapp.com/', include('main.urls')),
]
