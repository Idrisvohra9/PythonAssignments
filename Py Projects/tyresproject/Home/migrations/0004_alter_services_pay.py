# Generated by Django 4.1.3 on 2022-12-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_services_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='pay',
            field=models.CharField(max_length=12),
        ),
    ]
