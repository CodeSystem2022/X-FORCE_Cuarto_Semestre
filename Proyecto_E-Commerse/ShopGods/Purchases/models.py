from django.db import models
from django.contrib.auth.models import User
from Product.models import Product


class Purchases(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)
    purchases_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.purchases_date} {self.user}'
