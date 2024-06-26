# Generated by Django 4.2.1 on 2024-03-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="number_of_comments",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="rate",
            field=models.CharField(
                blank=True, default="no rating", max_length=10, null=True
            ),
        ),
    ]
