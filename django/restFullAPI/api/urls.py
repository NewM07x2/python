from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import CustomerInfoViewSet
# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
router.register('customer', CustomerInfoViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('customerInfo/', include(router.urls)),
]
