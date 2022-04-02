from dataclasses import field
from site import check_enableusersite
from statistics import mode
from rest_framework import serializers
from . import models

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name']

