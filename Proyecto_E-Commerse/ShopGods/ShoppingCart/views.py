from .models import ShoppingCart, ShoppingCartProduct
from Product.views import getProductById, thereIsStock
from django.shortcuts import get_object_or_404
from MyUser.views import getUserByUsername
from django.http import HttpResponse
from django.db.models import Q

def getShoppingCartByUsername(username: str):
    try:
        user = getUserByUsername(username=username) # Modificar por metodo creado en user
        shoppingCart = get_object_or_404(ShoppingCart,user=user)
        return shoppingCart
    except Exception as e:
        return e
    
def getProductsOfShoppingCart(username: str):
    try:
        shoppingCartProducts = ShoppingCartProduct.objects.select_related('shoppingCart__user').filter(shoppingCart__user__username=username)
        return shoppingCartProducts
    except Exception as e:
        return e

# Cada vez que se realiza una compra se debe crear un carrito pero antes borrarlo
def createShoppingCart(user):
    try:
        if ShoppingCart.objects.filter(user=user).count() == 0:
            shoppingCart = ShoppingCart(user=user)
            shoppingCart.save()
            return True
        else:
            return False
    except Exception as e:
        return e
    
def addProductToShoppingCart(username: str, product_param: any):
    try:
        print('Aca 1')
        product = getProductById(product_param['id'])
        condition = Q(product__id=product_param['id']) & Q(shoppingCart__user__username=username)
        shoppingCartProduct = ShoppingCartProduct.objects.filter(condition)[:1]
        print('Aca 2')
        print('shoppingCartProduct', shoppingCartProduct)
        if shoppingCartProduct:
            print('Aca Existe')
            print(shoppingCartProduct[0])
            product_param['amount'] = product_param['amount'] + shoppingCartProduct[0].amount
            thereIs = thereIsStock(product=product , amount=product_param['amount'])
            if thereIs['stock'] == True:
                shoppingCartProduct[0].amount = product_param['amount']
                shoppingCartProduct[0].save()
                return True
            if thereIs['stock'] == False:
                print('No hay stock pero existe')
                return False
        thereIs = thereIsStock(product=product , amount=product_param['amount'])
        if thereIs['stock'] == True:
            print('Aca No existe pero hay stock')
            shoppingCart = getShoppingCartByUsername(username)
            shoppingCartProduct = ShoppingCartProduct(shoppingCart=shoppingCart, product=product, amount=product_param['amount'])
            shoppingCartProduct.save()
            return True
        if thereIs['stock'] == False:
            print('No hay stock')
            return False
    except Exception as e:
        return e
    
def deleteItemOfShoppingCart(id_shopping_cart_product: int):
    try:
        ShoppingCartProduct.objects.filter(id=id_shopping_cart_product).delete()
        return True
    except Exception as e:
        return e
    
def deteleShoppingCart(username: str):
    try:
        response = ShoppingCart.objects.filter(user__username=username).delete()
        if response[0] > 0:    
            return True
        if response[0] == 0:
            return False
    except Exception as e:
        return e
    


def test(request):
    print('Se comienza la prueba')
    
    # Se prueba la creacion de un carrito
    # result = createShoppingCart('jeroalvarez1')
    # print('result', result)
    # La prueba funciona correctamente
    
    # Se prueba la agregacion de productos al carrito
    # response = addProductToShoppingCart(username='jeroalvarez1', product_param={'id': 2, 'amount': 2})
    # print(response)
    # La prueba funciona correctamente
    
    # Se prueba la funcion para listar los procutos de un carrito de compras
    # response = getProductsOfShoppingCart('jeroalvarez1')
    # print(response)
    # for item in response:
    #     print(item.product.id)
    # Fucniona correctamente
    
    # Prueba borrar un shoppingCart
    # response = deteleShoppingCart('jeroalvarez1')
    # print(response)
    
    print('Se finalizo la prueba')
    return HttpResponse('Esta funcionando correctamento')