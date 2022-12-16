# Generated by Django 4.1.3 on 2022-12-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('pname', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
