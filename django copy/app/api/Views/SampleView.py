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
from ..Models.Models import Sample
from ..Serializer.Serializer import SampleSerializer


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