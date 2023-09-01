from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include  # 追加
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),

    # アプリ毎にルーティング処理を行う。
    path('album/', include('album.urls')),
    path('app/', include('app.urls')),
    path('api/', include('api.urls')),

]
