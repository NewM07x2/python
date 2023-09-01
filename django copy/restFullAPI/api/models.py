# モデルはDjangoにてDBの構造を定義していくファイル

from unicodedata import category, name
from django.db import models

# クラス名がDB.テーブル名となる。


class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class CustomerInfo(models.Model):
    # ユーザ名
    frist_name = models.CharField(verbose_name='名', max_length=32)
    Last_name = models.CharField(verbose_name='姓', max_length=32)
    # 年齢
    age = models.IntegerField(verbose_name='年齢', null=True, unique=False)
    # 作成日時
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f"{self.frist_name} {self.Last_name}"
