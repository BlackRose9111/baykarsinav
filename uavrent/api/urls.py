from . import views
from django.urls import path

urlpatterns = [

    path("", views.api_home, name="api_home"),
    path("resttest/", views.rest_test, name="rest_test"),
    path("uavs/", views.get_all_uavs, name="get_all_uavs"),
]