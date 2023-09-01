from unicodedata import category, name
from django.db import models
# ユーザ情報を格納する


class UserInfo(models.Model):
    user_name = models.CharField(
        verbose_name='ユーザ名', max_length=32)                         # ユーザ名
    birth_day = models.DateField(
        verbose_name='生年月日')                                       # 生年月日
    age = models.PositiveSmallIntegerField(
        verbose_name='年齢', null=True, unique=False)         # 年齢
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
