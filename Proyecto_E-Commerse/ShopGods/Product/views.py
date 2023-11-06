from .models import Product, Key, Mail, Others
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet
from MyUser.views import getUserByUsername


def getProductById(id: int):
    try:
        product = get_object_or_404(Product,id=id)
        return product
    except Exception as e:
        return e
    
def getProducts(amount_per_page: int = 25, actual_page: int = 1, search: str = None):
    try:
        condition = Q(name__icontains=search)
        products = Product.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return products
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
        if type == 'key':
            items = Key.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        if type == 'mail':
            items = Mail.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        if type == 'others':
            items = Others.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return items   
    except Exception as e:
        return e

def createProduct(product_param):
    try:
        user = getUserByUsername(product_param["user"])
        product = Product(user=user, name=product_param["name"], price=product_param["price"]) 
        product.save()
        return product
    except Exception as e:
        return e     
         
def updateProduct(id, product_param):
    try:
        product = getProductById(id)
        product.name = product_param["name"]
        product.price = product_param["price"]
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
        return True
    except Exception as e:
        return e

# def payOrNotPlayProduct(id, pay):
#     try:
#         purchase = getPurchaseById(id)
#         purchase.pay = pay
#         return
#     except Exception as e:
#         return e

def test(request):
    print('Comenzo la prueba')
    
    #Importaciones
    from MyUser.views import createUser, login

    # Pruebas de registrarse y loguearse

    # print('Crear un usuario')
    # data = {
    #     'username': 'jeroalvarez11',
    #     'password': 'jerolindo',
    #     'email': 'jeroalvarez1@gmail.com'
    # }
    # print(createUser(data))
    # createUser funciona correctamente
    
    print('Loguearse')
    username = login('jeroalvarez1', 'jerolindo')
    # login funciona correctamente
    # views de MyUser funcionan correctamente
    
    # Pruebas de crear un produto y agregar items al mismo
    product_param = {
        'user': username,
        'name': 'Valorant points x1000',
        'price': 2000
    }
    id_product = createProduct(product_param).id
    
    items = [
        {
            'key': 'Qasdasjdkj1232134'
        },
        {
            'key': 'kjadsjhdsajhjk2'
        },
        {
            'key': 'jkadsjhajhads'
        }
    ]
    print(addItem('key', id_product, items))
    
    items = [
        {
            'mail': 'jeroalvarez1@gmail.com',
            'password': 'jero'
        },
        {
            'mail': 'piteralfonso@gmail.com',
            'password': 'jero'
        },
        {
            'mail': 'juanmerlo@gmail.com',
            'password': 'jero'
        }
    ]
    print(addItem('mail', id_product, items))
    
    items = [
        {
            'description': 'description 1'
        },
        {
            'description': 'description 2'
        },
        {
            'description': 'description 3'
        }
    ]
    print(addItem('others', id_product, items))
    
    # El proceso de crear un producto y luego agregarle items en base a su id funciona correctamente
    
    
    
    print('Se finalizo la prueba')
    return HttpResponse('Esta funcionando correctamento')




