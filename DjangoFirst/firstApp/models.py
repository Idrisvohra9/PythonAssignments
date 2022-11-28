from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id = models.AutoField
    product_name = models.CharField(max_length=120)
    product_price = models.IntegerField(default=100)
    mfc_date = models.DateField()