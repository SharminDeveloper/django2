# Generated by Django 4.2.1 on 2024-03-02 00:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_product_number_of_comments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="user_commment",
            new_name="user_comment",
        ),
    ]