# Generated by Django 4.1.3 on 2022-11-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='', max_length=399),
        ),
    ]