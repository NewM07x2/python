from pyexpat import model
from django import views
from django.shortcuts import render
from django.views.generic import *
from rest_framework.permissions import *
from rest_framework.generics import *

from . import models
from . import serializers

# Create your views here.

class TopView(ListView):
    model = models.Weather
    template_name = 'top.html'
    

class weatherAPIView(RetrieveAPIView):
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer
    permission_classes = [IsAuthenticated]