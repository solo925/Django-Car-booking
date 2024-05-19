from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    booker=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    phone=models.CharField(max_length=11)

    
    # def __str__(self):
    #     return self.booker
    

class Brand(models.Model):
    brand_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.brand_name
    
    
    
class Car(models.Model):
    name=models.CharField(max_length=100)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    brand=models.ManyToManyField(Brand)
    image=models.ImageField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add =True)
    
    def __str__(self):
        return self.name
    
       
