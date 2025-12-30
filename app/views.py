from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.
# url = "http://127.0.0.1:8000/school_data"

# def home(request):
#     data = requests.get(url)
#     print("this is it")
#     print(data.json())
#     return render(request, 'home.html', {'data': data})

# import os
# BACKEND_API_BASE = os.environ.get(
#     "BACKEND_API_BASE",
#     "https://djangofrontend-production.up.railway.app/"  # fallback for production
# )

import logging

logger = logging.getLogger(__name__)

# API_URL = settings.BACKEND_API_URL  # use env variable
API_URL = "https://djangod-production.up.railway.app"  # use env variable

def home(request):
    data = []
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Backend API error: {e}")

    return render(request, "home.html", {"data": data})