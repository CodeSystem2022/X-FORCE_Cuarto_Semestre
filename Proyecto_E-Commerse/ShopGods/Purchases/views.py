from django.db import transaction
from Product.models import Key, Mail, Others
from django.shortcuts import get_object_or_404
from .models import Purchases
from django.db.models import Q
from ShoppingCart.views import deleteItemOfShoppingCart
from MyUser.views import *
from Product.views import thereIsStock, getItemsByProduct, updateProductStock
from django.http import HttpResponse
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
import sys
import json


class PayPalClient:
    def __init__(self, client_id, secret_key):
        self.client_id = client_id
        self.client_secret = secret_key

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(
            client_id=client_id, client_secret=secret_key)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key, value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                self.object_to_json(value) if not self.is_primittive(value) else\
                value
        return result

    def array_to_json_array(self, json_array):
        result = []
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if not self.is_primittive(item)
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, int)


# Obtener los detalles de la transacción
class GetOrder(PayPalClient):

    def __init__(self, client_id, secret_key):
        super().__init__(client_id, secret_key)

    # 2. Set up your server to receive a call from the client
    """You can use this function to retrieve an order by passing order ID as an argument"""

    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        # 3. Call PayPal to get the transaction
        response = self.client.execute(request)
        return response.result
        # 4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
        # print 'Status Code: ', response.status_code
        # print 'Status: ', response.result.status
        # print 'Order ID: ', response.result.id
        # print 'Intent: ', response.result.intent
        # print 'Links:'
        # for link in response.result.links:
        #   print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        # print 'Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
        #                    response.result.purchase_units[0].amount.value)


class CaptureOrder(PayPalClient):

    def __init__(self, client_id, secret_key):
        super().__init__(client_id, secret_key)

    # 2. Set up your server to receive a call from the client
    """this sample function performs payment capture on the order.
    Approved order ID should be passed as an argument to this function"""

    def capture_order(self, order_id, debug=False):
        """Method to capture order using order_id"""
        request = OrdersCaptureRequest(order_id)
        # 3. Call PayPal to capture an order
        response = self.client.execute(request)
        # 4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
        if debug:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Links: ')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            print('Capture Ids: ')
            for purchase_unit in response.result.purchase_units:
                for capture in purchase_unit.payments.captures:
                    print('\t', capture.id)
            print("Buyer:")
            # print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
            # response.result.payer.name.given_name + " " + response.result.payer.name.surname,
            # response.result.payer.phone.phone_number.national_number)
        return response


def getPurchaseById(id: int):
    try:
        purchases = get_object_or_404(Purchases, id=id)
        return purchases
    except Exception as e:
        return e


def getPurchasesByUsernameOfBuyer(username, amount_per_page: int = 10, actual_page: int = 1):
    try:
        condition = Q(user__username=username)
        products = Purchases.objects.filter(condition)[(
            amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return products
    except Exception as e:
        return e


def getPurchasesByIdSaler():
    return


# 1 - Debe preguntar si hay stock
# 2 - Debe crear la compra
# 3 - Debe resatarle restar el stock al producto
# 4 - Debe agregar el id de la compra a la key, others o mail
# 5 - Debe eliminar el producto del carrito
@transaction.atomic
def createPurchase(user_id: int, product: any, price: float, unit_price: float, amount: int, shopping_cart_product_id: int):
    try:
        print('Entra a compra')
        stock = thereIsStock(product=product, amount=amount)
        if stock['stock'] == False:
            print('No hay stock')
            return {'stock': False, 'product': product, 'actual_amount': stock['amount']}
        user = getUserById(user_id)
        purchase = Purchases(user=user, product=product,
                             price=price, unit_price=unit_price, amount=amount)
        purchase.save()
        product.stock = int(product.stock) - int(amount)
        product.save()
        print('Guarda la compra y el actualiza el prodcuto')
        if product.type == 'key':
            item_list = []
            items = getItemsByProduct(bought=True, type='key', actual_page=1,
                                      product=product, amount_per_page=int(amount))
            for i in items['items']:
                i.puschase = purchase
                item_list.append(i)
            Key.objects.bulk_update(item_list, ['puschase'])
        if product.type == 'mail':
            item_list = []
            items = getItemsByProduct(bought=True, type='mail', actual_page=1,
                                      product=product, amount_per_page=int(amount))
            for i in items['items']:
                i.puschase = purchase
                item_list.append(i)
            Mail.objects.bulk_update(item_list, ['puschase'])
        if product.type == 'others':
            item_list = []
            items = getItemsByProduct(bought=True, type='others', actual_page=1,
                                      product=product, amount_per_page=int(amount))
            for i in items['items']:
                i.puschase = purchase
                item_list.append(i)
            Others.objects.bulk_update(item_list, ['puschase'])
        print('Asigna todos los items')
        deleteItemOfShoppingCart(shopping_cart_product_id)
        print('Borra el producto y sale')
    except Exception as e:
        # Si ocurre algún error, se realiza un rollback
        print('Hace rolback')
        print(e)
        transaction.set_rollback(True)
        return {'error': str(e)}
    return {'success': True}

# def createPurchase(username: str):
#     try:
#         # Se obtiene el usuario
#         user = getUserByUsername(username=username)
#         # Se crea el objeto compra
#         purchases = Purchases(user=user)
#         # Se crea la lista de productos y pregunta si hay stock
#         shoppingCartProducts = getProductsOfShoppingCart(username=username)
#         purchase_product_list = []
#         for item in shoppingCartProducts:
#             stock = thereIsStock(product=item.product, amount=item.amount)
#             if stock['stock'] == False:
#                 return {'stock': False, 'product': item.product, 'actual_amount': stock['amount']}
#             purchase_product_list.append(PurchaseProduct(
#                 purchases=purchases, product=item.product, price=item.product.price, amount=item.amount))
#         # Se guarda la compra
#         purchases.save()
#         # Se guarda la lista de productos comprados
#         PurchaseProduct.objects.bulk_create(purchase_product_list)
#         # Relacionar el item con la compra
#         for purchase_product in purchase_product_list:
#             if purchase_product.product.type == 'key':
#                 item_list = []
#                 items = getItemsByProduct(bought=True, type='key', actual_page=1,
#                                           id_product=purchase_product.product, amount_per_page=purchase_product.amount)
#                 for i in items['items']:
#                     i.puschase = purchase_product.purchases
#                     item_list.append(i)
#                 print('aca 4')
#                 Key.objects.bulk_update(item_list, ['puschase'])
#                 print('aca 5')
#             if purchase_product.product.type == 'mail':
#                 item_list = []
#                 items = getItemsByProduct(bought=True, type='mail', actual_page=1,
#                                           id_product=purchase_product.product, amount_per_page=purchase_product.amount)
#                 for i in items['items']:
#                     i.puschase = purchase_product.purchases
#                     item_list.append(i)
#                 Mail.objects.bulk_update(item_list, ['puschase'])
#             if purchase_product.product.type == 'others':
#                 item_list = []
#                 items = getItemsByProduct(bought=True, type='others', actual_page=1,
#                                           id_product=purchase_product.product, amount_per_page=purchase_product.amount)
#                 for i in items['items']:
#                     i.puschase = purchase_product.purchases
#                     item_list.append(i)
#                 Others.objects.bulk_update(item_list, ['puschase'])
#             updateProductStock(product=purchase_product.product,
#                                add=False, amount=purchase_product.amount)

#         deteleShoppingCart(username=username)
#         return True
#     except Exception as e:
#         return e


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
