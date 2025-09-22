"""
Serializer definitions for the API app.
ここでは、モデルのシリアライザを定義する。(API入出力を変換するためのクラス)
必要があれば、バリデーションもここで行う。
fields = '__all__' とすると、モデルの全フィールドを含む。個別に指定することも可能。
例えば、fields = ['id', 'name'] のようにする。
"""
from rest_framework import serializers
from .models import User, Task, Test

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'