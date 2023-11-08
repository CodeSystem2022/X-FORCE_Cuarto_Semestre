from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    products =  models.ManyToManyField(Product, through='ShoppingCartProduct')
    
    def __str__(self):
        return f'{self.id} {self.user}'
    
#HACER RELACION CON PRODUCTO DONDE SE LE DEBE AGREGAR CANTIDAD
class ShoppingCartProduct(models.Model):
    shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(default=1, blank=False, null=False)
    
    def __str__(self):
        return f'{self.shoppingCart} {self.product}'
