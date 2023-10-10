from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    sales_quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
           
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.name
    
class SubSubCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False)
    product =  models.ManyToManyField(Product)
    
    def __str__(self):
        return self.name

    

    

