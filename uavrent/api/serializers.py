from rest_framework import serializers
from django.contrib.auth.models import User

from . import models
class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UAV
        fields = '__all__'


class UavCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UAVCategory
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #default user model
        model = User
        fields = ['id', 'username']

class RentSerializer(serializers.ModelSerializer):
    renter  = UserSerializer(many=False, read_only=True)
    uav = UavSerializer(many=False, read_only=True)
    class Meta:
        model = models.Rent
        fields = '__all__'

