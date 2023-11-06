from django.db import models
from django.contrib.auth.models import User
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    sales_quantity = models.IntegerField(blank=True, null=True)
    pay = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name

from Purchases.models import Purchases
class Key(models.Model):
    key = models.CharField(max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)  
    
class Mail(models.Model):
    mail = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)
    
class Others(models.Model):
     description = models.CharField(max_length=80, null=False, blank=False)
     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
     puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)
         