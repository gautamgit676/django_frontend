from django.urls import path, include
from app.views import create_user, home
urlpatterns = [
    path('', home, name='home'),
    path('userforms/', create_user, name='create_user'),
]
