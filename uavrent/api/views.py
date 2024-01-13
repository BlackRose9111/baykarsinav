from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import response as RestResponse
from rest_framework.decorators import api_view
from . import models, serializers
def api_home(request, *args, **kwargs):
    return JsonResponse({"name": "UAVRent API", "version": "0.0.1"})

@api_view(["GET"])
def rest_test(request, *args, **kwargs):
    return RestResponse.Response({"name": "UAVRent API", "version": "0.0.1"})

@api_view(["GET"])
def get_all_uavs(request, *args, **kwargs):
    uavs = models.UAV.objects.all()
    uavs = serializers.UavSerializer(uavs, many=True).data
    return RestResponse.Response({"uavs": uavs})