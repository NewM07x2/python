from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .Views import UserInfoViewSet, CustomerInfoViewSet, UserViewSet, GroupViewSet, SampleViewSet
# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
router.register(r'sample', SampleViewSet)
router.register(r'userInfo', UserInfoViewSet)
router.register(r'customerInfo', CustomerInfoViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    # サンプル機能
    path('sample', include(router.urls)),
    path('sample2', SampleViewSet.as_view({'get': 'list'}), name="sampleList"),
    path('sample/all', SampleViewSet.getSampleDataAllList, name="getSampleDataAllList"),
    path('sample/filter', SampleViewSet.getSampleDataFilterList, name="getSampleDataList"),
    path('sample/insert', SampleViewSet.insertSampleData, name="insertSampleData"),
    path('sample/bulkInsert', SampleViewSet.bulkInsertSampleData, name="BulkInsertSampleData"),
    path('sample/update', SampleViewSet.updateSampleData, name="updateSampleData"),
    path('sample/delete', SampleViewSet.deleteSampleData, name="deleteSampleData"),
    path('sample/deleteAll', SampleViewSet.deleteAllSampleData, name="deleteAllSampleData"),
    # ユーザ機能
    path('useInfo/', include(router.urls)),
    # 顧客機能
    path('customerInfo/', include(router.urls)),
]
