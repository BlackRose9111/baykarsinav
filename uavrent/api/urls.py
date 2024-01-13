from . import views
from django.urls import path

urlpatterns = [

    path("", views.api_home, name="api_home"),

]