from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

app_name = 'app'
urlpatterns = [
    path('1', views.TestAPI.as_view()),
    path('2', views.ListAPI.as_view()),
]
