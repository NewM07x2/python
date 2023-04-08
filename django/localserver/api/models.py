from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name + ' ' + self.age
