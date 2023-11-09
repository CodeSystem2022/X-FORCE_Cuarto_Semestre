import os

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from django.db import IntegrityError
from django.http import JsonResponse

from MyUser.views import createUser, login_access, getMyUserByUser, changeUser, deleteUserB, getUserByUsername
from Product.views import getProductById, createProduct, getProductsByUser, getProducts, updateProduct,deleteProductById

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
    response = createUser(user)
    print(response)
    if isinstance(response, IntegrityError):
        print('redirige a create user')
        return redirect("registerUser")
        
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
    print(product.photo)
    return render(request, "myProductEdit.html", context={"product": product, 'user': user, 'my_user': my_user})

def updateProductF(request):    #Modifica un producto
    id_product = request.POST.get("id_product")
    product = {
        'photo': request.FILES.get('filephoto'),
        'name': request.POST.get("txtname"),
        'type': request.POST.get("selecttype"),
        'description': request.POST.get("txtdescription"),
        'price': request.POST.get("numprice"),
        'user': request.user.username
    }
    print(product)
    product = updateProduct(id_product, product)
    return redirect("myProducts")

def deleteProduct(request, id_product):     #Borra un producto
    deleteProductById(int(id_product))
    return redirect ("main")

def product(request,id_product):        #Renderiza la página del producto
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    product = getProductById(id_product)
    return render(request, "product.html", context={"product": product, 'user': user, 'my_user': my_user})




#-------------------------------Referido a ShopCart---------------------------------------#


def myShopCart(request):
    return render(request, "myShopCart.html")


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