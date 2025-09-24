from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Task, Test
from .serializers import UserSerializer, TaskSerializer, TestSerializer


async def sampleSingleAsync():
    await asyncio.sleep(5)
    print("OK")

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    await sampleSingleAsync()

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

