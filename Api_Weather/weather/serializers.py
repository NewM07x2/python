from dataclasses import field
from site import check_enableusersite
from statistics import mode
from rest_framework import serializers
from . import models

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Weather
        fields = [
            'id', 
            'location',
            'weather',
            'temperature',
        ]

