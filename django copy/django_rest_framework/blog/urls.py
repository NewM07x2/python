# coding: utf-8
from rest_framework import routers
from .views import UserViewSet, EntryViewSet

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        # json で出力するフィールド
        fields = ('id', 'user_name', 'birth_day', 'age', 'created_at')
