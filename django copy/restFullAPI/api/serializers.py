from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import CustomerInfo


class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        # json で出力するフィールド
        fields = ('id', 'name', 'age', 'created_at')
