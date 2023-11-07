from Product.models import Product
from django.shortcuts import get_object_or_404
from .models import Purchases
from django.db.models import Q

def getPurchaseById(id: int):
    try:
        purchase = get_object_or_404(Purchases,id=id)
        return purchase
    except Exception as e:
        return e

def getPurchasesByIdOfBuyer(id_buyer, amount_per_page: int = 10, actual_page: int = 1,):
    try:
        condition = Q(user=id_buyer)
        products = Purchases.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return products
    except Exception as e:
        return e
    
def getPurchasesByIdSaler():
    return

def createPurchase(purchase_param):
    try:
        products = Product.objects.filter(id__in=purchase_param["products"])
        purchase = Purchases(user=purchase_param["user"]) 
        purchase.save()
        purchase.products.set(products)
        return True
    except Exception as e:
        return e
