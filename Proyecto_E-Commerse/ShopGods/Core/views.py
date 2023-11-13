
from django.http import HttpResponseRedirect
from django.urls import reverse
from Purchases.models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from MyUser.views import *
from Product.views import *
from ShoppingCart.views import *
from Purchases.views import *
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def login(request):
    return render(request, "login.html")


# def loginUser(request):
#     return render(request, "login.html")


def loginF(request):
    result = login_access(request, username=request.POST.get(
        "txtname"), password=request.POST.get("txtpassword"))
    if result:
        return redirect("main")
    else:
        return redirect("login")


def main(request):
    actual_page = request.GET.get('actual_page')
    if isinstance(request.user, AnonymousUser):
        products = getProducts(actual_page=int(
            actual_page) if actual_page else 1, amount_per_page=5, search='')
        context = {
            'products': products['products'],
            'actual_page': products['actual_page'],
            'page_amount': products['page_amount']
        }
    else:
        user = getUserByUsername(request.user.username)
        my_user = getMyUserByUser(user=user)
        products = getProducts(actual_page=int(
            actual_page) if actual_page else 1, amount_per_page=5, search='', username=user.username)
        context = {
            'my_user': my_user,
            'products': products['products'],
            'actual_page': products['actual_page'],
            'page_amount': products['page_amount']
        }
    return render(request, "main.html", context=context)


# ---------------------------Referido a Usuarios-------------------------------#

@login_required
def user(request, int_null):  # Renderiza la página de usuario
    # id = User.objects.get(id = iduser)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    alert = int(int_null)
    return render(request, "users.html", context={'user': user, 'my_user': my_user, "alert": alert})


def addUser(request):  # Renderiza la página de registrar usuario

    # if ((request.POST.get("txtname") == None) or (request.POST.get("txtpassword")==None) or (request.POST.get("txtmail") == none)):
    user = {
        'username': request.POST.get("txtname"),
        'password': request.POST.get("txtpassword"),
        'email': request.POST.get("txtmail")
    }
    user = createUser(user)
    if isinstance(user, IntegrityError):
        return redirect("registerUser")
    if isinstance(user, ValueError):
        return redirect("registerUser")
    createShoppingCart(user)
    return redirect("login")


def registerUser(request):  # Crea un nuevo usuario
    return render(request, "register.html")


@login_required
def editUser(request):  # Renderiza la página de editar usuario
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "usersEdit.html", context={'user': user, 'my_user': my_user})


def modifyUser(request):  # Modifica un usuario
    user = {

        'old_username': request.user.username,
        'email': request.POST.get("txtemail"),
        'password': request.POST.get("txtpassword"),
        'repassword': request.POST.get("txtrepassword"),
        'client_id': request.POST.get("txtclient_id"),
        'secret_key': request.POST.get('txtsecret_key'),
        'profile_photo': request.POST.get("txtphoto")
    }
    if not user["password"] or not user["repassword"]:
        response = changeUser(old_username=user["old_username"],
                              email=user["email"], client_id=user["client_id"], secret_key=user["secret_key"], profile_photo=user["profile_photo"])
        return redirect("user", int_null=0)
    if user["password"] == user["repassword"]:
        changeUser(old_username=user["old_username"], email=user["email"],
                   client_id=user["client_id"], secret_key=user["secret_key"], profile_photo=user["profile_photo"], password=user["password"])
        return redirect("login")


def deleteUser(request):  # Borra un usuario
    deleteUserB(request.user.username)
    return redirect("login")


# ------------------------------------Referido a Productos------------------------------------------

@login_required
def myProducts(request):  # Renderiza la página de los productos del usuario
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    products = getProductsByUser(user=user)
    return render(request, "myProducts.html", context={'user': user, 'my_user': my_user, 'products': products})


@login_required
def addProduct(request):  # Renderiza la página para agregar un nuevo producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "addProduct.html", context={'user': user, 'my_user': my_user})


@login_required
def addProduct2(request, msg):  # Renderiza la página para agregar un nuevo producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "addProduct.html", context={'user': user, 'my_user': my_user, msg: msg})


def createProductF(request):  # Crea un nuevo producto
    product = {
        'photo': request.FILES.get('filephoto'),
        'name': request.POST.get("txtname"),
        'type': request.POST.get("selecttype"),
        'description': request.POST.get("txtdescription"),
        'price': request.POST.get("numprice"),
        'user': request.user.username
    }
    product = createProduct(product)

    if product == False:
        msg = 'El producto no puedo ser creado correctamente'
        return redirect("addProduct2", msg=msg)
    else:
        product = createProduct(product)
        return redirect("myProducts")


@login_required
def myProductEdit(request, id_product):  # Renderiza la página para editar un producto
    product = getProductById(id_product)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    response = getItemsByProduct(
        product=product, type=product.type, amount_per_page=100000)
    return render(request, "myProductEdit.html", context={"product": product, 'user': user, 'my_user': my_user, 'items': response['items']})


@login_required
# Renderiza la página para editar un producto
def myProductEdit2(request, id_product, msg):
    product = getProductById(id_product)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    response = getItemsByProduct(
        product=product, type=product.type, amount_per_page=100000)
    return render(request, "myProductEdit.html", context={"product": product, 'user': user, 'my_user': my_user, 'items': response['items'], 'msg': msg})


def updateProductF(request):  # Modifica un producto
    id_product = request.POST.get("id_product")
    product = {
        'photo': request.FILES.get('filephoto'),
        'name': request.POST.get("txtname"),
        'description': request.POST.get("txtdescription"),
        'price': request.POST.get("numprice"),
        'user': request.user.username
    }
    product = updateProduct(id_product, product)
    return redirect("myProducts")


def deleteProduct(request, id_product):  # Borra un producto
    deleteProductById(id=id_product)
    return redirect("myProducts")


# Hacer algo para que funcione deslogueado
def product(request, id_product):  # Renderiza la página del producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    product = getProductById(id_product)
    context = {"product": product, 'user': user,
               'my_user': my_user, 'login': True}
    if isinstance(user, Http404):
        context['login'] = False
    return render(request, "product.html", context=context)


def createItem(request):    # Crear un item
    product = getProductById(request.POST.get("id_product"))
    field1 = request.POST.get("txtitemfield1")
    field2 = request.POST.get("txtitemfield2")
    data = {
        "msg": "Debe rellenar los campos para agregar un nuevo item"
    }
    if product.type == 'key':
        if not field1:
            return redirect("myProductEdit2", id_product=product.id, msg=data['msg'])
        item = [
            {
                'key': field1
            }
        ]
    if product.type == 'mail':
        if not field1 or not field2:
            return redirect("myProductEdit2", id_product=product.id, msg=data['msg'])
        item = [
            {
                'mail': field1,
                'password': field2
            }
        ]
    if product.type == 'others':
        if not field1:
            return redirect("myProductEdit2", id_product=product.id, msg=data['msg'])
        item = [
            {
                'description': field1
            }
        ]

    result = addItem(type=product.type, id_product=product.id, items=item)
    getItemsByProduct(product=product, type=product.type,
                      amount_per_page=100000)
    return redirect("myProductEdit", id_product=product.id)


def deleteItem(request, id_item, id_product, product_type):
    deleteItemById(id=id_item, type=product_type)
    return redirect("myProductEdit", id_product)
# -------------------------------Referido a ShopCart---------------------------------------#


# Agrega un producto al carrito
def addProductToShoppingCartF(request, id_product):
    product_param = {
        'id': id_product,
        'amount': int(request.POST.get("numAmount"))
    }
    result = addProductToShoppingCart(
        username=request.user.username, product_param=product_param)
    if result is True:
        return redirect("product", id_product=id_product)
    if result is False:
        return redirect("product", id_product=id_product)


def deleteShopCart(request, id_shopcart):  # Borra un producto del carrito
    deleteItemOfShoppingCart(id_shopcart)
    return redirect("myShopCart")
# def deleteItemOfShoppingCartF(request):


@login_required
def myShopCart(request):  # Renderiza la pagina del carrito de compra
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    shopping_cart_products = getProductsOfShoppingCart(user.username)
    print(shopping_cart_products)

    for shop_cart_product in shopping_cart_products:
        shop_cart_product.client_id = getMyUserByUser(
            shop_cart_product.product.user).client_id

    return render(request, "myShopCart.html", context={'user': user, 'my_user': my_user, 'shopping_cart_products': shopping_cart_products})


@login_required
def myShopCart2(request, mensaje):  # Renderiza la pagina del carrito de compra
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    shopping_cart_products = getProductsOfShoppingCart(user.username)
    print(shopping_cart_products)

    for shop_cart_product in shopping_cart_products:
        shop_cart_product.client_id = getMyUserByUser(
            shop_cart_product.product.user).client_id

    return render(request, "myShopCart.html", context={'user': user, 'my_user': my_user, 'shopping_cart_products': shopping_cart_products, 'mensaje': mensaje})

# hay que modificar funcion delete product para que no borre si tiene una compra


def pago(request):
    # Debe buscar si el usaurio actual tiene una compra cerrar
    # Si esta cerrada debe crear una nueva, y si esta abierta debe agregar agregar productos
    try:
        print('Entro a pago')
        data = json.loads(request.body)
        order_id = data['orderID']
        product_id = data['product_id']
        amount = data['amount']
        shopping_cart_product_id = data['shopping_cart_product_id']
        product = getProductById(product_id)
        my_user = getMyUserByUserId(user_id=product.user.id)

        print('order_id', order_id)
        print('my_user.client_id', my_user.client_id)
        print('my_user.secret_ke', my_user.secret_key)
        # Hay que preguntar si hay stock
        response = thereIsStock(product=product, amount=amount)
        print(response)
        if response['stock'] == False:
            mensaje = "No se pudo realizar la compra porque no hay stock"
            return JsonResponse({'mensaje': mensaje, 'redirect_url': reverse('myShopCart2', args=[mensaje])})
        detail = GetOrder(my_user.client_id,
                          my_user.secret_key).get_order(order_id)
        print(detail)
        # detail_price = float(detail.result.purchase_units[0].amount.value)
        # if detail_price == product.price * amount:
        trx = CaptureOrder(my_user.client_id, my_user.secret_key).capture_order(
            order_id, debug=True)
        createPurchase(user_id=request.user.id, product=product, price=float(product.price) *
                       int(amount), unit_price=product.price, amount=amount, shopping_cart_product_id=shopping_cart_product_id)
        # data = {
        #     "id": f"{trx.result.id}",
        #     "nombre_cliente": f"{trx.result.payer.name.given_name}",
        #     "mensaje": "Compra realizada exitosamente"
        # }
        print('Va a redirigir')
        return JsonResponse({'mensaje': 'Compra realizada exitosamente', 'redirect_url': reverse('myShopCart')})
    except Exception as e:
        print(e)
        mensaje = f"Error {e}"
        return JsonResponse({'mensaje': mensaje, 'redirect_url': reverse('myShopCart2', args=[mensaje])})
    # else:
    #     data = {
    #         "mensaje": "No se pudo realizar la compra"
    #     }
    #     return redirect("myShopCart")


def payShopCart(request, id_shopping_cart):

    print('id_shopping_cart', id_shopping_cart)

    return redirect("myShopCart")


# -------------------------------Referido a historial-------------------------------#

@login_required
def myRecord(request):         # Renderiza la pagina del historial
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    buy = request.GET.get('buy')
    if buy == '1':
        historyProduct = Purchases.objects.filter(user=user)
        buy = True
    else:
        historyProduct = Purchases.objects.filter(product__user=user)
        buy = False

    return render(request, "myRecord.html", {"purchases": historyProduct, 'user': user, 'my_user': my_user, 'buy': buy})


@login_required
def historyBuy(request, id_record):      # Renderiza la pagina del producto del historial
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    historyProduct = Purchases.objects.get(id=id_record)
    if historyProduct.product.type == 'key':
        items = Key.objects.filter(puschase=historyProduct)
    if historyProduct.product.type == 'mail':
        items = Mail.objects.filter(puschase=historyProduct)
    if historyProduct.product.type == 'others':
        items = Others.objects.filter(puschase=historyProduct)

    print(items[0].product.type)
    return render(request, "historybuy.html", context={"historyProduct": historyProduct, 'my_user': my_user, 'productType': historyProduct.product.type, 'items': items})


# -------------------------------Referido a funciones varias-------------------------------#

def darkMode(request):
    DarkMode = request.POST.get("nightDaySlider") == 'on'
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    my_user.dark_mode = DarkMode
    my_user.save()
    return render(request, "users.html", context={'user': user, 'my_user': my_user})


def formNull(request, int_null):
    return redirect("user", int_null=int_null)


def check_empty_form(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            # Si algún campo del formulario tiene un valor, no está vacío
            if value:
                return False
        # Todos los campos del formulario están vacíos
        return True
    # No es una solicitud POST
    return None
