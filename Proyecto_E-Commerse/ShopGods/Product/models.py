from django.db import models
from django.contrib.auth.models import User
from Purchases.models import Purchases
from Company.models import Company

class Label(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    sales_quantity = models.IntegerField(blank=True, null=True)
    label =  models.ManyToManyField(Label, blank=True, null=True)
    company = models.ForeignKey(Company, blank=False, null=False)
        
    def __str__(self):
        return self.name
           
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.name
    
class SubSubCategory(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False, blank=False)
    product =  models.ManyToManyField(Product, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Key(models.Model):
    key = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschases = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=False, null=False)  
    
class Mail(models.Model):
    mail = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
    puschases = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=False, null=False)
    
class Others(models.Model):
     description = models.CharField(max_length=80)
     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)   
     puschases = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=False, null=False)
         