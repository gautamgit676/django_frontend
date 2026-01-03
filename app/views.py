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


def userdatas(request):
    url = f"{BACKEND_API_BASE}userdata/"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.RequestException as e:
        logger.error("Backend API error: %s", e)
        data = {
            "message": "Service unavailable",
            "data": ""
        }
    return render(request, "userdata.html", {"data": data})


# # create user frontend api
def create_user(request):
    url = f"{BACKEND_API_BASE}userform/"
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
