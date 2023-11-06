from .models import ShoppingCart
from Product.views import getProductById
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def getShoppingCartByUserId(id_user: int):
    try:
        user = get_object_or_404(User, id=id) # Modificar por metodo creado en user
        shoppingCart = get_object_or_404(ShoppingCart,user=user)
        return shoppingCart
    except Exception as e:
        return e

def createShoppingCart(shoppingCart):
    try:
        shoppingCart = ShoppingCart(user=shoppingCart['user'])
        shoppingCart.save()
        return True
    except Exception as e:
        return e
    
def addProductToShoppingCart(id_user: int, id_product: int):
    try:
        shoppingCart = getShoppingCartByUserId(id_user)
        product = getProductById(id_product)
        shoppingCart.product.set(product)
        shoppingCart
        return True
    except Exception as e:
        return e
    
def deteleShoppingCart(id_user: int):
    try:
        shoppingCart = getProductById(id_user)
        shoppingCart.delete()
    except Exception as e:
        return e