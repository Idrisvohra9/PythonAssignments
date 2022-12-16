from django.db import models

# makemgrations - create changes and store in a file.
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name+self.email
    
class Services(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    pname = models.CharField(max_length=122)
    pay = models.CharField(max_length=12)
    date = models.DateField()
    
    def __str__(self):
        return self.name+' '+self.pname
    