# Generated by Django 4.1.3 on 2022-11-28 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="mfc_date",
            field=models.DateField(),
        ),
    ]
