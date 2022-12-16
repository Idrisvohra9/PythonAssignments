from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    """
    Modal for inserting fruits.
    """
    User_id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=30)
    Email = models.EmailField(max_length=120)
    Password = models.CharField(max_length=10)
    DOB = models.DateField()

class Product_fruit(models.Model):
    """
    Modal for inserting fruits.
    """
    fruit_Id = models.AutoField(primary_key=True)
    fruit_image = models.ImageField()
    fruit_name = models.CharField(max_length=120)
    fruit_real_price = models.IntegerField(default=150)
    fruit_dis_price = models.IntegerField(default=100)
    delTimeFrom = models.DateTimeField()
    delTimeTo = models.DateTimeField()
    deliveryDay = models.CharField(max_length=120)
    
class Product_veggie(models.Model):
    """
    Modal for inserting vegetables.
    """
    veggie_Id = models.AutoField(primary_key=True)
    veggie_image = models.ImageField()
    veggie_name = models.CharField(max_length=120)
    veggie_real_price = models.IntegerField(default=150)
    veggie_dis_price = models.IntegerField(default=100)
    delTimeFrom = models.DateTimeField()
    delTimeTo = models.DateTimeField()
    deliveryDay = models.CharField(max_length=120)
    