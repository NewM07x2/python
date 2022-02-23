from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # topページにアクセスしたらviewのindex()を返却する。
    path('', views.index),  # 新規追加
    path('test', views.test),  # 新規追加
]
