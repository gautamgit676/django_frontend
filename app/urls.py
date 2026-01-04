from django.urls import path, include
from app.views import home,create_user, studentforms,userdatas,mainpage
urlpatterns = [
    path('home/', home, name='home'),
    # path('', mainpage, name='mainpage'),
    path('userf/', create_user, name='create_user'),
    path('userdetails/', userdatas, name='userdetails'),
    path('studentform/', studentforms, name='studentforms'),
]
