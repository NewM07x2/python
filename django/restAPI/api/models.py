"""
ここにはDBのテーブル定義を記述する。
追加したら、makemigrations, migrateを実行してDBに反映させる。

python manage.py makemigrations;
python manage.py migrate;
python manage.py showmigrations;

python manage.py makemigrations; python manage.py migrate;

python manage.py dbshell
→ Django経由でpostgreSQLに入れる。
"""

import uuid
from django.db import models

class User(models.Model):

    class Meta:
        db_table = 'user'
        ordering = ['created_date',]
        verbose_name = verbose_name_plural = 'ユーザー'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
  """ Task model
  id : primary key
  task_name : task name
  importance : importance of task
  """

  class Meta:
    db_table = 'task'
    ordering = ['created_date',]
    verbose_name = verbose_name_plural = 'タスク'
  
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  task_name = models.CharField(verbose_name='TitleName', max_length=50, unique=True)
  task_detail = models.CharField(verbose_name='TitleDetail', max_length=255, null=True)
  status = models.CharField(verbose_name='Status', max_length=10, null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.task_name

class Test(models.Model):
  """ Test model
  id : primary key
  content : test
  importance : importance of test
  """

  class Meta:
    db_table = 'test'
    ordering = ['created_date',]
    verbose_name = verbose_name_plural = 'テスト'

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  content = models.CharField(verbose_name='Content', max_length=20, unique=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.id)