# Generated by Django 4.2.1 on 2024-02-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customusermodel",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]