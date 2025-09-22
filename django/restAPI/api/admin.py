from django.contrib import admin

# Register your models here.
from .models import User, Task, Test

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'mail', 'created_date', 'updated_date',)
  ordering = ('-created_date',)
  readonly_fields = ('id', 'created_date', 'updated_date',)

class TaskModelAdmin(admin.ModelAdmin):
  list_display = ('task_name', 'task_detail', 'status', 'created_date', 'updated_date',)
  ordering = ('-created_date',)
  readonly_fields = ('id', 'created_date', 'updated_date',)

class TestModelAdmin(admin.ModelAdmin):
  list_display = ('content', 'created_date', 'updated_date',)
  ordering = ('-created_date',)
  readonly_fields = ('id', 'created_date', 'updated_date',)

admin.site.register(User, UserModelAdmin)
admin.site.register(Task, TaskModelAdmin)
admin.site.register(Test, TestModelAdmin)
