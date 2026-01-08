from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.


# API_URL = settings.BACKEND_API_URL  # use env variable

from pro.settings import BACKEND_API_BASE
import logging
logger = logging.getLogger(__name__)


def mainpage(request):
    return render(request, "main.html")


def Userapicreate(request):
    url = f"{BACKEND_API_BASE}userapi/"
    try:
        r = requests.post(url, timeout=5)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "userform.html", {"data": data})

def Usersdata(request):
    url = f"{BACKEND_API_BASE}userapi/"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        logger.info("Fetched user data: %s", data)
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "userdata.html", {"data": data})



def User_Profile(request):
    url = f"{BACKEND_API_BASE}userprofiles/"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        logger.info("Fetched user profile data: %s", data)
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "userprofile.html", {"data": data})



def loginuser(request):
    url = f"{BACKEND_API_BASE}login/"
    try:
        r = requests.post(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        logger.info("User login response: %s", data)
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "userlogin.html", {"data": data})

# # # create user frontend api
# def UserCreate(request):
#     url = f"{BACKEND_API_BASE}userdata/"
#     l= requests.get(url)
#     url = f"{BACKEND_API_BASE}userform/"
#     try:
#         r = requests.post(url, timeout=5)
#         r.raise_for_status()
#         data = r.json()
#     except requests.exceptions.RequestException as e:
#         logger.error("Backend API error: %s", e)
#         data = {
#             "message": "Service unavailable",
#             "data": ""
#         }
#     return render(request, "userform.html", {"data": l})



def home(request):
    url = f"{BACKEND_API_BASE}demoapi/"
    # data = {} # Default empty data
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()   # ✅ JSON → Python dict
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "home.html", {"data": data})


# def userdatas(request):
#     url = f"{BACKEND_API_BASE}userdata/"
#     try:
#         r = requests.get(url, timeout=5)
#         r.raise_for_status()
#         data = r.json()
#         logger.info("Fetched user data: %s", data)
#     except requests.exceptions.RequestException as e:
#         logger.error("Backend API error: %s", e)
#         data = {
#             "message": "Service unavailable",
#             "data": ""
#         }
#     return render(request, "userdata.html", {"data": data})




# sudent form fillform
# def studentforms(request):
#     url = f"{BACKEND_API_BASE}studentform/"
#     try:
#         r = requests.post(url, timeout=5)
#         r.raise_for_status()
#         data = r.json()
#         logger.info("Fetched user data: %s", data)
#     except requests.exceptions.RequestException as e:
#         logger.error("Backend API error: %s", e)
#         data = {
#             "message": "Service unavailable",
#             "data": ""
#         }
#     return render(request, "studentadd.html", {"data": data})


# def create_student(request):
#     # 1️⃣ Fetch FK data (users)
#     users_url = f"{BACKEND_API_BASE}userdata/"  # or User API
#     fk_data = []
#     try:
#         r = requests.get(users_url, timeout=5)
#         r.raise_for_status()
#         fk_data = r.json()
#     except Exception as e:
#         logger.error("Failed to fetch FK data: %s", e)

#     # 2️⃣ Handle form POST
#     response_data = {}
#     if request.method == "POST":
#         student_url = f"{BACKEND_API_BASE}stu/"
#         payload = {
#             "user": request.POST.get("user"),  # FK id
#             "full_name": request.POST.get("full_name"),
#             "roll_number": request.POST.get("roll_number"),
#             "date_of_birth": request.POST.get("date_of_birth"),
#             "address": request.POST.get("address"),
#             "phone_number": request.POST.get("phone_number")
#         }

#         try:
#             r = requests.post(student_url, json=payload, timeout=5)
#             r.raise_for_status()
#             response_data = r.json()
#         except requests.exceptions.RequestException as e:
#             logger.error("Backend API error: %s", e)
#             response_data = {"message": "Service unavailable"}

#     return render(
#         request,
#         "studentadd.html",
#         {"fk_data": fk_data, "response_data": response_data}
#     )
