from django.db import models
from django.contrib.auth.models import User
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(blank=True, default=0)
    sales_quantity = models.IntegerField(blank=True, null=True)
    pay = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='static/product/', default='static/product/default.jpg')
    type = models.CharField(max_length=50, blank=False, null=False)
        
    def __str__(self):
        return f'{self.id} - {self.name}'

from Purchases.models import Purchases
class Key(models.Model):
    key = models.CharField(max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.key
    
class Mail(models.Model):
    mail = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.mail
class Others(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschase = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=True, null=True)
     
    def __str__(self):
        return self.description