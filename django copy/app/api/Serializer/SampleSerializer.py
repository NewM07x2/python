from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..Models.Models import Sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'
