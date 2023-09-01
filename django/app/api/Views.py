from django.contrib.auth.models import User, Group
from django.http.response import JsonResponse
# rest_framework関連
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# 各種定義
import json
from .Models import UserInfo
from .Models import CustomerInfo
from .Models import Sample

from .Serializer import UserInfoSerializer
from .Serializer import CustomerInfoSerializer
from .Serializer import UserSerializer
from .Serializer import GroupSerializer
from .Serializer import SampleSerializer

from .Logic import CreateSampleModelObject

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


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @api_view(['GET']) # GET のみに対応
    def getSampleDataAllList(request):
        # モデルからデータを抽出する
        allData = Sample.objects.all()
        # シリアライザにデータを渡す
        serializer = SampleSerializer(allData, many=True) 
        # シリアル可されたデータを return で返す
        return JsonResponse(serializer.data, safe=False)

    @api_view(['GET']) # GET のみに対応
    def getSampleDataFilterList(request):
        data = request.data
        # モデルからデータを抽出する
        filter_data = Sample.objects.filter(id__gte=27, id__lte=29)
        # シリアライザにデータを渡す
        serializer = SampleSerializer(filter_data, many=True) 
        # シリアル可されたデータを return で返す
        return JsonResponse(serializer.data, safe=False)

    @api_view(['POST'])
    def insertSampleData(request):
        if request.method == 'POST':
            # POSTリクエストからデータを取得
            data = request.data
            # バリデーションを行ったり、データを整形したりすることができます
            try:
                # データベースにデータを挿入
                new_item = Sample.objects.create(
                    title=data['title'],
                    description=data['description']
                )
                return Response({"status": "success", "data": request.data}, status=status.HTTP_200_OK)
            except Exception as e:
                # エラー時のレスポンス
                return Response({"message": str(e)}, status=400)
        print('---end---')
        # POST以外のメソッドへの対応
        return Response({"message": "Method not allowed!!!"}, status=405)  

    @api_view(['POST'])
    def bulkInsertSampleData(request):
        if request.method == 'POST':
            data = request.data
            try:
                Insert_List = CreateSampleModelObject(data)
                # データベースにデータを一括挿入
                Sample.objects.bulk_create(Insert_List)
                return Response({"status": "success", "data": request.data}, status=status.HTTP_200_OK)
            except Exception as e:
                # エラー時のレスポンス
                return Response({"message": str(e)}, status=400)
        print('---end---')
        # POST以外のメソッドへの対応
        return Response({"message": "Method not allowed!!!"}, status=405)  

    @api_view(['PUT'])
    def updateSampleData(request):
        if request.method == 'PUT':
            data = request.data
            # バリデーションを行ったり、データを整形したりすることができます
            try:
                sample = Sample.objects.get(id=data['id'])
                serializer = SampleSerializer(sample, data=data)
                if not serializer.is_valid():
                    return JsonResponse(serializer.errors, status=400)
                serializer.save()
            except Sample.DoesNotExist:
                return Response({"message": "Item not found"}, status=404)

            return Response({"message": "Item updated successfully"}) 

    @api_view(['DELETE'])
    def deleteSampleData(request):
        if request.method == 'DELETE':
            try:
                data = request.data
                sample = Sample.objects.get(id=data['id'])
            except Sample.DoesNotExist:
                return Response({"message": "Item not found"}, status=404)
            # データベースのフィールドを削除
            sample.delete()

            return Response({"message": "Item updated successfully"}) 

    @api_view(['DELETE'])
    def deleteAllSampleData(request):
        if request.method == 'DELETE':
            try:
                # データベースのフィールドを削除
                Sample.objects.all().delete()
            except Sample.DoesNotExist:
                return Response({"message": "Item not found"}, status=404)

            return Response({"message": "Item updated successfully"}) 


