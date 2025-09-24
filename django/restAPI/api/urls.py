from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # get example
    path('get/user/', UserViewSet.as_view({'get': 'list'})), # APIView
    
    # post example
    path('post/user/', UserViewSet.as_view({'post': 'create'})), # APIView

]
