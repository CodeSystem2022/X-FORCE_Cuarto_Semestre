from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product =  models.ManyToManyField(Product, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user} {self.product}'
    

    
