from .models import Product, Key, Mail, Others
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from MyUser.views import getUserByUsername
from Purchases.models import PurchaseProduct
import math


def getProductById(id: int):
    try:
        product = get_object_or_404(Product,id=id)
        return product
    except Exception as e:
        return e
    
def getProductsByUser(user):
    try:
        products = Product.objects.filter(user=user)
        return products
    except Exception as e: 
        return e
    
def getProducts(amount_per_page: int = 25, actual_page: int = 1, search: str = '', username: str = None):
    try:
        condition = (Q(name__icontains=search) | Q(description__icontains=search)) & ~Q(user__username=username)
        products = Product.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        page_amount = math.ceil(Product.objects.filter(condition).count() / amount_per_page)
        response = {
            'products': products,
            'actual_page': actual_page,
            'page_amount': page_amount
        }
        return response
    except Exception as e:
        return e

def getItemById(id: int, type: str):
    try:
        item = None
        if type == 'key':
            item = get_object_or_404(Key,id=id)
        if type == 'mail':
            item = get_object_or_404(Mail,id=id)
        if type == 'others':
            item = get_object_or_404(Others,id=id)
        return item
    except Exception as e:
        return e

def getItemsByProductId(id_product: int, type: str, bought: bool = None, amount_per_page: int = 25, actual_page: int = 1):
    try:
        product = getProductById(id_product)
        condition = Q(product=product)
        if bought is True:
            condition &= Q(puschase__isnull=True)
        if bought is False:
            condition &= Q(puschase__isnull=False)
        items = []        
        page_amount = 0
        if type == 'key':
            items = Key.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
            page_amount = math.ceil(Key.objects.filter(condition).count() / amount_per_page)
        if type == 'mail':
            items = Mail.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
            page_amount = math.ceil(Mail.objects.filter(condition).count() / amount_per_page)
        if type == 'others':
            items = Others.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
            page_amount = math.ceil(Others.objects.filter(condition).count() / amount_per_page)
        response = {
            'items': items,
            'actual_page': actual_page,
            'page_amount': page_amount
        }
        return response   
    except Exception as e:
        return e

# obtener el item donde el id product == a x y la compra sea igual a x
def getItemByIdProductAndIdPurchase(id_product: int, id_purchase: int, type: str):
    try:
        items = None
        condition = Q(product__id=id_product) & Q(puschase__id=id_purchase)
        if type == 'key':
            items = Key.objects.filter(condition)
            return items
        if type == 'mail':
            items = Mail.objects.filter(condition)
            return items
        if type == 'others':
            items = Others.objects.filter(condition)
            return items
    except Exception as e:
        return e

def createProduct(product_param):
    try:
        user = getUserByUsername(product_param["user"])
        product = Product(user=user, name=product_param["name"], price=product_param["price"], type=product_param["type"], description=product_param["description"], photo=product_param["photo"] if product_param["photo"] is not None else 'static/product/default.jpg') 
        product.save()
        return product
    except Exception as e:
        return e     
         
def updateProduct(id, product_param):
    try:
        product = getProductById(id)
        product.name = product_param["name"]
        product.price = product_param["price"]
        product.type = product_param["type"]
        product.description = product_param["description"]
        if product_param["photo"]:
            product.photo = product_param["photo"]
        product.save()
        return product
    except Exception as e:
        return e
    
def updateItem(id: int, type: str, item_param: any):
    try:
        item = getItemById(id=id, type=type)
        if type == 'key':
            item.key = item_param['key']
        if type == 'mail':
            item.mail = item_param['mail']
            item.password = item_param['password']
        if type == 'others':
            item.description = item_param['description']
        item.save()
        return item
    except Exception as e:
        return e
    
# Funciona que actualiza el stock del producto cuando se agrega o borra un item
def updateProductStock(product, add: bool = None, amount: int = 0):
    try:
        if add == True:
            product.stock = product.stock + amount
        if add == False:
            product.stock = product.stock - amount
        product.save()
        return True
    except Exception as e:
        return e
    
def addItem(type, id_product, items):
    try:
        product = getProductById(id_product)
        items_list = []
        if type == 'key':        
            for key in items:
                items_list.append(Key(key=key['key'], product=product))
            Key.objects.bulk_create(items_list)
        if type == 'mail':
            for mail in items:
                items_list.append(Mail(mail=mail['mail'], password=mail['password'], product=product))
            Mail.objects.bulk_create(items_list)
        if type == 'others':
            for others in items:
                items_list.append(Others(description=others['description'], product=product))
            Others.objects.bulk_create(items_list)
        if len(items_list) > 0:
            updateProductStock(product=product, add=True, amount=len(items_list))
        return True
    except Exception as e:
        return e
    
# Funcion borrar producto siempre y cuando no haya sido comprado
def deleteProductById(id: int):
    try:
        product = getProductById(id)
        purchased_product_count = PurchaseProduct.objects.filter(product=product).count()
        if purchased_product_count == 0:
            product.delete()
            return True
        else:
            return False
    except Exception as e:
        return e
    
# Funcion borrar un item siempre y cuando no haya sido comprado
def deleteItemById(id: int, type: str):
    try:
        item = getItemById(id, type)
        if item.puschase is None:
            product = item.product
            item.delete()
            updateProductStock(product=product, add=False, amount=1)
            return True
        else:
            return False
    except Exception as e:
        return e
    
# Funcion que pregunta si hay stock
def thereIsStock(product, amount):
    try:
        stock = {
            'stock': amount <= product.stock,
            'amount': product.stock
        }
        return stock
    except Exception as e:
        return e

def test(request):
    print('Comenzo la prueba')
    
    #Importaciones
    from MyUser.views import createUser, login

    # Pruebas de registrarse y loguearse

    # print('Crear un usuario')
    # data = {
    #     'username': 'jeroalvarez1',
    #     'password': 'Jero2002?',
    #     'email': 'jeroalvarez1@gmail.com'
    # }
    # print(createUser(data))
    # createUser funciona correctamente
    
    # print('Loguearse')
    # username = login('jeroalvarez1', 'Jero2002?')
    # login funciona correctamente
    # views de MyUser funcionan correctamente
    
    # Pruebas de crear un produto y agregar items al mismo
    # product_param = {
    #     'user': username,
    #     'name': 'Valorant points Last',
    #     'price': 2000
    # }
    # id_product = createProduct(product_param).id
    
    # Arreglar actualizar stock
    
    # items = [
    #     {
    #         'key': 'Qasdasjdkj1232134'
    #     },
    #     {
    #         'key': 'kjadsjhdsajhjk2'
    #     },
    #     {
    #         'key': 'jkadsjhajhads'
    #     }
    # ]
    # print(addItem('key', id_product, items))
    
    # items = [
    #     {
    #         'mail': 'jeroalvarez1@gmail.com',
    #         'password': 'jero'
    #     },
    #     {
    #         'mail': 'piteralfonso@gmail.com',
    #         'password': 'jero'
    #     },
    #     {
    #         'mail': 'juanmerlo@gmail.com',
    #         'password': 'jero'
    #     }
    # ]
    # print(addItem('mail', id_product, items))
    
    # items = [
    #     {
    #         'description': 'description 1'
    #     },
    #     {
    #         'description': 'description 2'
    #     },
    #     {
    #         'description': 'description 3'
    #     }
    # ]
    # print(addItem('others', id_product, items))
    # El proceso de crear un producto y luego agregarle items en base a su id funciona correctamente
    
    # Pruebas de listar productos
    # products = getProducts(amount_per_page=7, actual_page= 1)
    # print(products)
    # # Prueba lista productos funciona correctamente

    # # Prueba de actualizar un producto
    # product = updateProduct(products['products'][6].id, {'name': 'Valo modificado', 'price': 20})
    # print(product)
    
    # # Prueba seleccionar un producto y ver el producto y luego ver todos sus items
    # items = getItemsByProductId(id_product=product.id, type='key', amount_per_page=10000, actual_page=1)
    # print(items)
    # # Prueba seleccionar un item y actualizarlo
    # item = getItemById(items['items'][0].id, 'key')
    # print(item)
    
    # item = updateItem(id=item.id, type='key', item_param={'key': 'jjjjjjjjjjj'})
    # print(item)
    # Todas las pruebas anteriores son exitosas
    
    # Prueba borar un producto que no haya sido comprado, borra items primero y luego producto 
    # response = deleteProductById(19)
    # print(f'El producto producto con id = {19} borrado? {response}')
    # Prueba exitosa
    
    # Prueba borrar un item siempre y cuando el mismo no haya sido comprado
    # response = deleteItemById(id=32, type='key')
    # print(f'Item borrado? {response}')
    # Funciona correctamente
    
    # Se prueba que cuando se agrega una lista de items a un producto se actualice el stock del producto
    
    # items = [
    #     {'mail': 'mail1@gmail.com', 'password': '1234'},
    #     {'mail': 'mail2@gmail.com', 'password': '1234'},
    #     {'mail': 'mail3gmail.com', 'password': '1234'}
    # ]
    # result = addItem(type='mail', id_product=id_product, items=items)
    # print('Se agrgaron los items?', result)
    # Funciona correctamente
    
    # Se prueba que cuando se quita un item de un producto se actualice el stock del producto
    # result = deleteItemById(id=2, type='mail')
    # print('Item borrado?', result)
    # Pruebas funcionan correctamente
    
    print('Se finalizo la prueba')
    return HttpResponse('Esta funcionando correctamento')




