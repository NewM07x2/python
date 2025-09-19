from django.db import models

# Create your models here.
# ここにモデルを定義していく。
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
