# Generated by Django 4.1.3 on 2022-11-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstApp", "0003_product_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormModel",
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
                ("fname", models.CharField(max_length=40)),
                ("lname", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=10)),
            ],
        ),
    ]
