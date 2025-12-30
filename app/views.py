from django.shortcuts import render
import requests
# Create your views here.
url = "http://127.0.0.1:8000/school_data"

def home(request):
    data = requests.get(url)
    print("this is it")
    print(data.json())
    return render(request, 'home.html', {'data': data})

