from rest_framework import viewsets
from .models import CustomerInfo
from .serializers import CustomerInfoSerializer


class CustomerInfoViewSet(viewsets.ModelViewSet):
    # モデルのオブジェクトを取得
    queryset = CustomerInfo.objects.all()
    # シリアライザーを取得
    serializer_class = [
        CustomerInfoSerializer
    ]
