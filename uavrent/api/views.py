from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"name": "UAVRent API", "version": "0.0.1"})
