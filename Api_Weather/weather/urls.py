from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('top/', views.TopView.as_view()),
    path('api/<int:pk>', views.weatherAPIView.as_view()),
]
