from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name    
    
    
class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    price = models.IntegerField()
    srtdesc = models.CharField(max_length=225)
    qty=models.IntegerField(default=50)
    desc =models.TextField()
    timestamp= models.DateTimeField(default=now)
    
    def __str__(self):
        return self.name;  
    
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    desc = models.TextField(max_length=300,default="")
    
    def __str__(self):
        return self.sub + " by " + self.email
    
class orders(models.Model):
    pass

class addCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()

class Order(models.Model):
    pass
