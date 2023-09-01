# モデルはDjangoにてDBの構造を定義していくファイル

from unicodedata import category, name
from django.db import models

# migrateするとデフォルトで機能名_クラス名がテーブル名となる。
# meteでdb_table名を変更することができる。
# これは機能間で共通テーブルのみで使用する。

class UserInfo(models.Model):
    class Meta:
        db_table = 'user_info'
    
    user_name = models.CharField(verbose_name='ユーザ名', max_length=32)
    birth_day = models.DateField(verbose_name='生年月日')
    age = models.PositiveSmallIntegerField(verbose_name='年齢', null=True, unique=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)


class Sample(models.Model):
    class Meta:
        db_table = 'sample'
        verbose_name = 'サンプル'
        verbose_name_plural = '00.サンプル'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title


class CustomerInfo(models.Model):
    class Meta:
        db_table = 'customer_info'
    
    frist_name = models.CharField(verbose_name='名', max_length=32)
    Last_name = models.CharField(verbose_name='姓', max_length=32)
    age = models.IntegerField(verbose_name='年齢', null=True, unique=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f"{self.frist_name} {self.Last_name}"
    

class Customer_Detail(models.Model):
    class Meta:
        db_table = 'customer_detail'

    frist_name = models.CharField(verbose_name='名', max_length=32)
    Last_name = models.CharField(verbose_name='姓', max_length=32)
    age = models.IntegerField(verbose_name='年齢', null=True, unique=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return f"{self.frist_name} {self.Last_name}"
