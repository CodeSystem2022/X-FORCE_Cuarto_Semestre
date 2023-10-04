from django.db import models
from django.contrib.auth.models import User

class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    purchases_date = models.DateTimeField(auto_now_add=True)
    card_data = models.TextField(null=True)
    
    
class PurchaseProduct(models.Model):
    Purchases = models.ForeignKey