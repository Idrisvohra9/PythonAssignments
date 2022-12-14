# Generated by Django 4.1.3 on 2022-12-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HaideriGreens", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product_fruit",
            fields=[
                ("fruit_Id", models.AutoField(primary_key=True, serialize=False)),
                ("fruit_image", models.ImageField(upload_to="")),
                ("fruit_name", models.CharField(max_length=120)),
                ("fruit_real_price", models.IntegerField(default=150)),
                ("fruit_dis_price", models.IntegerField(default=100)),
                ("delTimeFrom", models.DateTimeField()),
                ("delTimeTo", models.DateTimeField()),
                ("deliveryDay", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Product_veggie",
            fields=[
                ("veggie_Id", models.AutoField(primary_key=True, serialize=False)),
                ("veggie_image", models.ImageField(upload_to="")),
                ("veggie_name", models.CharField(max_length=120)),
                ("veggie_real_price", models.IntegerField(default=150)),
                ("veggie_dis_price", models.IntegerField(default=100)),
                ("delTimeFrom", models.DateTimeField()),
                ("delTimeTo", models.DateTimeField()),
                ("deliveryDay", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("User_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
