from django.contrib import admin

# Register your models here.
from .Models import CustomerInfo, Sample

# 管理画面上でテーブルを表示する。
@admin.register(CustomerInfo)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    pass