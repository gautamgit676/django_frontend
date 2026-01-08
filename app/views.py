from django.shortcuts import render ,redirect
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
    if request.method == "POST":
        url = f"{BACKEND_API_BASE}userapi/"

        payload = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "phone_number": request.POST.get("phone_number"),
            "role": request.POST.get("role"),  # shopkeeper / customer
            "password": request.POST.get("password"),
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            r = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=5
            )

            if r.status_code == 400:
                return render(request, "userform.html", {
                    "error": r.json()
                })

            r.raise_for_status()
            data = r.json()

            logger.info("User registered successfully: %s", data)

            return redirect("userlogin")

        except requests.exceptions.RequestException as e:
            logger.error("Backend API error: %s", e)
            return render(request, "userform.html", {
                "error": "Service unavailable"
            })

    return render(request, "userform.html")

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
    if request.method == "POST":
        url = f"{BACKEND_API_BASE}userprofiles/"

        token = request.session.get("access")
        if not token:
            return redirect("login")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        data = {
            "address": request.POST.get("address"),
            "shop_name": request.POST.get("shop_name"),
            "pincode": request.POST.get("pincode"),
            "city": request.POST.get("city"),
            "state": request.POST.get("state"),
            "country": request.POST.get("country"),
        }

        files = {}
        if request.FILES.get("profile_image"):
            files["profile_image"] = request.FILES["profile_image"]

        try:
            r = requests.post(
                url,
                data=data,      # ✅ form-data
                files=files,    # ✅ file upload
                headers=headers,
                timeout=10
            )
            r.raise_for_status()
            response_data = r.json()

            logger.info("Profile saved: %s", response_data)
            return redirect("mainpage")

        except requests.exceptions.HTTPError:
            logger.error("Backend error: %s", r.text)
            return render(request, "userprofile.html", {
                "error": "Invalid data submitted"
            })

        except requests.exceptions.RequestException as e:
            logger.error("Backend API error: %s", e)
            return render(request, "userprofile.html", {
                "error": "Service unavailable"
            })

    return render(request, "userprofile.html")

logger = logging.getLogger(__name__)

def loginuser(request):
    if request.method == "POST":
        url = f"{BACKEND_API_BASE}login/"

        payload = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            r = requests.post(url, json=payload, headers=headers, timeout=5)
            r.raise_for_status()
            data = r.json()

            # ✅ store token in session
            request.session["access"] = data.get("access")
            request.session["refresh"] = data.get("refresh")

            return redirect("mainpage")

        except requests.exceptions.HTTPError:
            logger.error("Backend error response: %s", r.text)
            data = {"message": "Invalid username or password"}

        except requests.exceptions.RequestException as e:
            logger.error("Backend API error: %s", e)
            data = {"message": "Service unavailable"}

        return render(request, "userlogin.html", {"data": data})

    return render(request, "userlogin.html")

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
