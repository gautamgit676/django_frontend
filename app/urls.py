from django.urls import path, include
from app.views import home
urlpatterns = [
    path('home', home, name='home'),
    # path('userforms/', create_user, name='create_user'),
]
