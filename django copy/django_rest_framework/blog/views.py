# coding: utf-8

from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import CustomerInfo
from .serializer import CustomerInfoSerializer


from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class CustomerInfoViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = CustomerInfo.objects.all()
    # シリアライザーを取得
    serializer_class = [
        CustomerInfoSerializer
    ]
