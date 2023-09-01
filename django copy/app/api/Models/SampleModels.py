# モデルはDjangoにてDBの構造を定義していくファイル

from unicodedata import category, name
from django.db import models

# migrateするとデフォルトで機能名_クラス名がテーブル名となる。
# meteでdb_table名を変更することができる。
# これは機能間で共通テーブルのみで使用する。

class Sample(models.Model):
    class Meta:
        db_table = 'sample'
        verbose_name = 'サンプル'
        verbose_name_plural = '00.サンプル'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
