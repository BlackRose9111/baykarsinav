from rest_framework import serializers
from django.contrib.auth.models import User

from . import models


class UavSerializerWithCategoryAsPrimaryKey(serializers.ModelSerializer):
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
        fields = ['id', 'username', "email"]

class UavSerializer(serializers.ModelSerializer):

    category = UavCategorySerializer(read_only=True, many=False)
    class Meta:
        model = models.UAV
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    renter  = UserSerializer(many=False)
    uav = UavSerializer(many=False)
    class Meta:
        model = models.Rent
        fields = '__all__'


class RentSerializerWithPrimaryKey(serializers.ModelSerializer):
    class Meta:
        model = models.Rent
        fields = '__all__'