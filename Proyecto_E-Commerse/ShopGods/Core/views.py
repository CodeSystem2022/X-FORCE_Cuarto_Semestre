import os

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import QueryDict
from MyUser.views import *
from Product.views import *
from ShoppingCart.views import *
# Create your views here.




def home(request):
    return render(request, "login.html")



# def loginUser(request):
#     return render(request, "login.html")



def loginF(request):
    print('None?',request.POST.get("txtname"))
    result = login_access(request, username=request.POST.get("txtname"), password=request.POST.get("txtpassword"))
    if result:
        return redirect("main")
    else:
        return redirect("home")
    
def main(request):
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    actual_page = request.GET.get('actual_page')
    print('actual_page', actual_page)
    products = getProducts(actual_page=int(actual_page) if actual_page else 1, amount_per_page=10, search='', username=user.username)
    return render(request, "main.html", context={'user': user, 'my_user': my_user, 'products': products['products'], 'actual_page': products['actual_page'], 'page_amount': products['page_amount']})



#---------------------------Referido a Usuarios-------------------------------#


def user(request):          #Renderiza la página de usuario
    #id = User.objects.get(id = iduser)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "users.html", context={'user': user, 'my_user': my_user})

def addUser(request):       #Renderiza la página de registrar usuario
    user = {
        'username': request.POST.get("txtname"),
        'password': request.POST.get("txtpassword"),
        'email': request.POST.get("txtmail")
    }
    user = createUser(user)
    if isinstance(user, IntegrityError):
        print('redirige a create user')
        return redirect("registerUser")
    createShoppingCart(user)
    print('redirige a login')
    return redirect("home")

def registerUser(request):  #Crea un nuevo usuario
    return render(request, "register.html")

def editUser(request):      #Renderiza la página de editar usuario
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "usersEdit.html", context={'user': user, 'my_user': my_user})

def modifyUser(request):    #Modifica un usuario
    user = {
        'username': request.POST.get("txtusername"),
        'old_username': request.user.username,
        'email': request.POST.get("txtemail"),
        'password': request.POST.get("txtpassword"),
        'repassword': request.POST.get("txtrepassword"),
        'cbu': request.POST.get("txtcbu"),
        'profile_photo': request.POST.get("txtphoto")
    }
    if not user["password"] or not user["repassword"]:
        response = changeUser(username=user["username"], old_username=user["old_username"], email=user["email"], cbu=user["cbu"], profile_photo=user["profile_photo"])
        print('response', response)
        return redirect("user")
    if user["password"] == user["repassword"]:
        changeUser(username=user["username"], old_username=user["old_username"], email=user["email"], cbu=user["cbu"], profile_photo=user["profile_photo"], password=user["password"])
        return redirect("home")

def deleteUser(request):    #Borra un usuario
   deleteUserB(request.user.username)
   return redirect("home")
        

#------------------------------------Referido a Productos------------------------------------------


def myProducts(request):    #Renderiza la página de los productos del usuario
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    products = getProductsByUser(user=user)
    return render(request, "myProducts.html", context={'user': user, 'my_user': my_user, 'products': products})

def addProduct(request):    #Renderiza la página para agregar un nuevo producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "addProduct.html", context={'user': user, 'my_user': my_user})

def createProductF(request):    #Crea un nuevo producto
    product = {
        'photo': request.FILES.get('filephoto'),
        'name': request.POST.get("txtname"),
        'type': request.POST.get("selecttype"),
        'description': request.POST.get("txtdescription"),
        'price': request.POST.get("numprice"),
        'user': request.user.username
    }
    print(product)
    product = createProduct(product)
    print(product)
    return redirect("myProducts")

def myProductEdit(request, id_product):     #Renderiza la página para editar un producto
    product = getProductById(id_product)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    response = getItemsByProduct(product=product, type=product.type, amount_per_page=100000)
    return render(request, "myProductEdit.html", context={"product": product, 'user': user, 'my_user': my_user, 'items': response['items']})

def updateProductF(request):    #Modifica un producto
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

def deleteProduct(request, id_product):     #Borra un producto
    deleteProductById(id=id_product)
    return redirect ("myProducts")

def product(request,id_product):        #Renderiza la página del producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    product = getProductById(id_product)
    return render(request, "product.html", context={"product": product, 'user': user, 'my_user': my_user})

def createItem(request):    # Crear un item
    print('Creando Item')
    product = getProductById(request.POST.get("id_product"))
    field1 = request.POST.get("txtitemfield1")
    field2 = request.POST.get("txtitemfield2")
    if product.type == 'key':
        item = [
            {
                'key': field1
            }
        ]
    if product.type == 'mail':
        item = [
            {
                'mail': field1,
                'password': field2
            }
        ]
    if product.type == 'others':
        item = [
            {
                'description': field1
            }
        ]
        
    result = addItem(type=product.type, id_product=product.id, items=item)
    print(result)
    getItemsByProduct(product=product, type=product.type, amount_per_page=100000)
    return redirect("myProductEdit", id_product=product.id)


def deleteItem(request, id_item, id_product, product_type):
    deleteItemById(id=id_item, type=product_type)
    return redirect("myProductEdit", id_product)
#-------------------------------Referido a ShopCart---------------------------------------#

def myShopCart(request):
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    shopping_cart_products = getProductsOfShoppingCart(user.username)
    print(shopping_cart_products)
    return render(request, "myShopCart.html", context={'user': user, 'my_user': my_user, 'shopping_cart_products': shopping_cart_products})

def addProductToShoppingCartF(request, id_product):
    product_param = {
        'id': id_product,
        'amount': int(request.POST.get("numAmount"))
    }
    print('product_param', product_param)
    result = addProductToShoppingCart(username=request.user.username, product_param=product_param)
    if result is True:
        return redirect("product", id_product=id_product)
    if result is False:
        return redirect("product", id_product=id_product)


def deleteShopCart(request, id_shopcart):
    deleteItemOfShoppingCart(id_shopcart)
    return redirect("myShopCart")
# def deleteItemOfShoppingCartF(request):
#     

#-------------------------------Referido a funciones varias-------------------------------#
def darkMode(request):
    DarkMode = request.POST.get("nightDaySlider") == 'on'
    print ('DarkMode', DarkMode)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    print (my_user)
    my_user.dark_mode = DarkMode
    my_user.save()
    return render(request, "users.html", context={'user': user, 'my_user': my_user})