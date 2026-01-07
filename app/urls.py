from django.urls import path, include
from app.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('', mainpage, name='mainpage'),
    path('userf/', UserCreate, name='userf'),
    path("demoapi/", demoapi, name="demoapi"   ),
    # path('userdetails/', userdatas, name='userdetails'),
    # path('student/', create_student, name='student'),
]
