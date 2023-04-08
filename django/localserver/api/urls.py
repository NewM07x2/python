from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

app_name = 'api'
urlpatterns = [
    path('1', views.TestAPI.as_view()),
    path('getName', views.ListAPI.as_view()),
]
