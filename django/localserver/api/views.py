from django.shortcuts import render
from django.views.generic import *

from rest_framework import serializers
from rest_framework import views
from rest_framework import generics
from . import models
from . import serializers

class TestAPI(views.APIView):
    permission_class = []

class ListAPI(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.TestSerializer
    permission_class = []

