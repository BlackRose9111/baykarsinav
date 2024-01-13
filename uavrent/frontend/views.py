from django.shortcuts import render
from datetime import date
# Create your views here.

API_ENDPOINT = "http://localhost:8000/api/"

GITHUB_URL = "https://github.com/BlackRose9111/baykarsinav.git"

def home(request):
    # frontend/templates/frontend/index.html

    context ={

        "current_date" : date.today(),
        "api_endpoint" : API_ENDPOINT,
        "github_url" : GITHUB_URL,
    }
    return render(request, "index.html", context=context)

