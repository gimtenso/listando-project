from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('https://listando.netlify.app/admin/', admin.site.urls),
    path('https://listando.netlify.app/', include('main.urls')),
]
