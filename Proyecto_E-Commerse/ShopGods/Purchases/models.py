from django.db import models
from django.contrib.auth.models import User
from Product.models import Product

class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    purchases_date = models.DateTimeField(auto_now_add=True)
    card_data = models.TextField(null=True, blank=True)
    product = models.ManyToManyField(Product, through='PurchaseProduct')
    
    def __str__(self):
        return f'{self.purchases_date} {self.user}'
    
    
class PurchaseProduct(models.Model):
    purchases = models.ForeignKey(Purchases, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    destination_mail = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.purchases} {self.product}'
    
    
    