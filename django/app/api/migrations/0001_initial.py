# Generated by Django 4.1 on 2023-08-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer_Detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("frist_name", models.CharField(max_length=32, verbose_name="名")),
                ("Last_name", models.CharField(max_length=32, verbose_name="姓")),
                ("age", models.IntegerField(null=True, verbose_name="年齢")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
            ],
            options={
                "db_table": "customer_detail",
            },
        ),
        migrations.CreateModel(
            name="CustomerInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("frist_name", models.CharField(max_length=32, verbose_name="名")),
                ("Last_name", models.CharField(max_length=32, verbose_name="姓")),
                ("age", models.IntegerField(null=True, verbose_name="年齢")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
            ],
            options={
                "db_table": "customer_info",
            },
        ),
        migrations.CreateModel(
            name="Sample",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
            ],
            options={
                "db_table": "sample",
            },
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=32, verbose_name="ユーザ名")),
                ("birth_day", models.DateField(verbose_name="生年月日")),
                ("age", models.PositiveSmallIntegerField(null=True, verbose_name="年齢")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
            ],
            options={
                "db_table": "user_info",
            },
        ),
    ]
