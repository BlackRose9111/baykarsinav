from rest_framework import serializers

from . import models
class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UAV
        fields = '__all__'

