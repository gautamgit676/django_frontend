from django.urls import path, include
from app.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('', mainpage, name='mainpage'),
    path('userf/', Userapicreate, name='userf'),
    # path("demoapi/", demoapi, name="demoapi"   ),
    path('userdetails/', Usersdata, name='userdetails'),
    path('profiles/', User_Profile, name='profiles'),
    path('userlogin/', loginuser, name='userlogin'),
    # path('student/', create_student, name='student'),
]
