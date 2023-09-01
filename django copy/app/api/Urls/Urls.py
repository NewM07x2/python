from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .Views import views
from ..Views.views import UserInfoViewSet, CustomerInfoViewSet, UserViewSet, GroupViewSet, SampleView
from ..Views.SampleView import SampleView
# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
router.register(r'sample', SampleView)
router.register(r'userInfo', UserInfoViewSet)
router.register(r'customerInfo', CustomerInfoViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    # サンプル機能
    path('sample', include(router.urls)),
    path('sample2', views.SampleView.as_view({'get': 'list'}), name="sampleList"),
    path('sample3', views.dataList, name="sampleList"),
    # ユーザ機能
    path('useInfo/', include(router.urls)),
    # 顧客機能
    path('customerInfo/', include(router.urls)),
]
