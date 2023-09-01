from django.contrib.auth.models import User, Group
from django.http.response import JsonResponse
# rest_framework関連
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# 各種定義
import json
from ..Models.Models import UserInfo, CustomerInfo, Sample
from ..Serializer.Serializer import UserInfoSerializer, CustomerInfoSerializer, UserSerializer, GroupSerializer, SampleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    

# ALTER ROLE postgres WITH PASSWORD 'postgres';
class UserInfoViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = UserInfo.objects.all()
    # シリアライザーを取得
    serializer_class = [
        UserInfoSerializer
    ]


class CustomerInfoViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = CustomerInfo.objects.all()
    # シリアライザーを取得
    serializer_class = [
        CustomerInfoSerializer
    ]


class SampleView(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET']) # GET のみに対応
def dataList(request):
    # モデルからデータを抽出する
    api_data = Sample.objects.all()
    # シリアライザにデータを渡す
    serializer = SampleSerializer(api_data, many=True) 
    # シリアル可されたデータを return で返す
    return JsonResponse(serializer.data, safe=False)