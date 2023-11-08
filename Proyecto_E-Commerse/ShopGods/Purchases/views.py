from Product.models import Key, Mail, Others
from django.shortcuts import get_object_or_404
from .models import Purchases, PurchaseProduct
from django.db.models import Q
from ShoppingCart.views import getProductsOfShoppingCart, deteleShoppingCart
from MyUser.views import getUserByUsername
from Product.views import thereIsStock, getItemsByProductId, updateProductStock
from django.http import HttpResponse

def getPurchaseById(id: int):
    try:
        purchases = get_object_or_404(Purchases,id=id)
        return purchases
    except Exception as e:
        return e

def getPurchasesByUsernameOfBuyer(username, amount_per_page: int = 10, actual_page: int = 1):
    try:
        condition = Q(user__username=username)
        products = Purchases.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return products
    except Exception as e:
        return e
    
def getPurchaseProductsByIdPurchase(id_purchase: int):
    try:
        purchasesProducts = PurchaseProduct.objects.filter(purchases__id=id_purchase)
        return purchasesProducts
    except Exception as e:
        return e
    
# Debe devolver que persona me compro que producto y cuando
# Debe obtener la compra pero solo los productos y los items de ese producto en donde el id_user del producto sea mio
def getPurchasesByIdSaler():
    return

# Falta preguntar si hay stock
def createPurchase(username: str):
    try:
        # Se obtiene el usuario
        user = getUserByUsername(username=username)
        # Se crea el objeto compra
        purchases = Purchases(user=user)
        # Se crea la lista de productos y pregunta si hay stock
        shoppingCartProducts = getProductsOfShoppingCart(username=username)
        purchase_product_list = []
        for item in shoppingCartProducts:
            stock = thereIsStock(product=item.product, amount=item.amount)
            if stock['stock'] == False:
                return {'stock': False, 'product': item.product, 'actual_amount': stock['amount']}
            purchase_product_list.append(PurchaseProduct(purchases=purchases, product=item.product, price=item.product.price, amount=item.amount))
        # Se guarda la compra
        purchases.save()
        # Se guarda la lista de productos comprados
        PurchaseProduct.objects.bulk_create(purchase_product_list)
        # Relacionar el item con la compra 
        for purchase_product in purchase_product_list:
            if purchase_product.product.type == 'key':
                item_list = []
                items = getItemsByProductId(bought=True, type='key', actual_page=1, id_product=purchase_product.product.id, amount_per_page=purchase_product.amount)
                for i in items['items']:
                    i.puschase = purchase_product.purchases
                    item_list.append(i)
                print('aca 4')
                Key.objects.bulk_update(item_list, ['puschase'])
                print('aca 5')
            if purchase_product.product.type == 'mail':
                item_list = []
                items = getItemsByProductId(bought=True, type='mail', actual_page=1, id_product=purchase_product.product.id, amount_per_page=purchase_product.amount)
                for i in items['items']:
                    i.puschase = purchase_product.purchases
                    item_list.append(i)
                Mail.objects.bulk_update(item_list, ['puschase'])
            if purchase_product.product.type == 'others':
                item_list = []
                items = getItemsByProductId(bought=True, type='others', actual_page=1, id_product=purchase_product.product.id, amount_per_page=purchase_product.amount)
                for i in items['items']:
                    i.puschase = purchase_product.purchases
                    item_list.append(i)
                Others.objects.bulk_update(item_list, ['puschase'])
            updateProductStock(product=purchase_product.product, add=False, amount=purchase_product.amount)
            
        deteleShoppingCart(username=username)
        return True
    except Exception as e:
        return e

def test(request):
    print('Proceso completo del sistema')
    
    from MyUser.views import createUser, login
    from Product.views import createProduct, addItem, getItemByIdProductAndIdPurchase
    from ShoppingCart.views import createShoppingCart, addProductToShoppingCart
    
    # # Crear un usuario 
    # data = {
    #     'username': 'jeroalvarez1',
    #     'password': 'Jero2002?',
    #     'email': 'jeroalvarez1@gmail.com'
    # }
    # createUserResponse = createUser(data)
    # print('¿Usuario creado?', createUserResponse)
    
    # # Loguearse como ese usuario
    # username = login('jeroalvarez1', 'Jero2002?')
    
    # # Agregar productos como ese usuario
    # product_param = {
    #     'user': username,
    #     'name': 'Product 1',
    #     'price': 10,
    #     'type': 'key'
    # }
    
    # id_product = createProduct(product_param).id

    # items = [
    #     {
    #         'key': 'Key 1'
    #     },
    #     {
    #         'key': 'Key 2'
    #     },
    #     {
    #         'key': 'Key 3'
    #     }
    # ]
    # print('Items del Producto 1 agregados', addItem('key', id_product, items))
    
    # product_param = {
    #     'user': username,
    #     'name': 'Product 2',
    #     'price': 10,
    #     'type': 'key'
    # }
    
    # id_product = createProduct(product_param).id

    # items = [
    #     {
    #         'key': 'Key 4'
    #     },
    #     {
    #         'key': 'Key 5'
    #     },
    #     {
    #         'key': 'Key 6'
    #     }
    # ]
    # print('Items del Producto 2 agregados', addItem('key', id_product, items))
    
    # # Todo lo anterior funciona correctamente
    
    # # Crear otro usuario
    # data = {
    #     'username': 'pedrocomprador',
    #     'password': 'Jero2002?',
    #     'email': 'jeroalvarez1@gmail.com'
    # }
    # createUserResponse = createUser(data)
    # print('¿Usuario creado?', createUserResponse)
    
    # # Loguearse como ese usuario
    # username = login('pedrocomprador', 'Jero2002?')
    
    # # Crear carrito de compra
    
    # result = createShoppingCart(username)
    # print('¿Carrito creado?', result)
    
    # # Agregar productos al carrito 
    # # Posible error en donde producto se puede agregar muchas veces al carrito antes de agreegar nuevo verificar si el producto ya fue agregago
    # response = addProductToShoppingCart(username=username, product_param={'id': 2, 'amount': 2})
    # print('¿Producto 2 agregado?', response)
    
    # response = addProductToShoppingCart(username=username, product_param={'id': 2, 'amount': 1})
    # print('¿Producto 2 agregado?', response)
    
    # response = addProductToShoppingCart(username=username, product_param={'id': 1, 'amount': 2})
    # print('¿Producto 1 agregado?', response)
    
    # # Comprar productos como ese usuario 
    # # Falta pagar compra
    
    # response = createPurchase(username)
    # print('¿Se compro?', response)
    
    # Se prueba obtener las compras de un comprador
    
    # purchases = getPurchasesByUsernameOfBuyer(username='pedrocomprador', actual_page=1, amount_per_page=100)
    # print(purchases)
    # print(purchases[0].id)
    # purchaseProducts = getPurchaseProductsByIdPurchase(purchases[0].id)
    # print(purchaseProducts)
    # for item in purchaseProducts:
    #     print(item.product.name)
    #     items = getItemByIdProductAndIdPurchase(id_product=item.product.id, id_purchase=item.purchases.id, type=item.product.type)
    #     for i in items:
    #         print(i)
    # obtener el item donde el id product == a x y la compra sea igual a x
    
    return HttpResponse('Proceso finalizado')