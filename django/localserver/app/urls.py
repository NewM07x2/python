from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

app_name = 'app'
urlpatterns = [
    # topページにアクセスしたらviewのindex()を返却する。
    path('', views.index, name='index'),  # 新規追加
    path('file', views.file, name='file'),  # 新規追加
    path('home', views.home, name='home'),  # 新規追加
    path('sample1', views.sample1, name='sample1'),  # 新規追加
    path('sample2', views.sample2, name='sample2'),  # 新規追加
    # path('test', views.test),  # 新規追加

    
]
