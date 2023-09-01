from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..Models.Models import UserInfo, CustomerInfo, Sample
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # json で出力するフィールド
        fields = ('id', 'user_name', 'birth_day', 'age', 'created_at')


class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        # json で出力するフィールド
        fields = ('id', 'name', 'age', 'created_at')
