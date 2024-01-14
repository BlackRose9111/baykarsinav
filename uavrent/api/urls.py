
from . import views
from django.urls import path


urlpatterns = [

    path("", views.api_home, name="api_home"),
    path("uav/", views.uav, name="get_uav"),
    path("rent/", views.rent, name="get_rent"),
    path("user/", views.user, name="get_user"),
    path("uavcategory/", views.uav_category, name="get_uavcategory"),
    path("test/", views.get_all, name="test"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("getmyuser/", views.get_my_user, name="get_my_user"),

]