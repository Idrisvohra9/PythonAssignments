from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=399)
    type=models.CharField(max_length=399,default="")
    description=models.CharField(max_length=300,default="")

    def __str__(self) :
        return self.name
    # date=models.DateField()