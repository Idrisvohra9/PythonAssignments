from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id = models.AutoField
    product_name = models.CharField(max_length=120)
    product_price = models.IntegerField(default=100)
    mfc_date = models.DateField()
    
class FormModel(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=10)