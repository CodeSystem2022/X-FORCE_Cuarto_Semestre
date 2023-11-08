import os

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404
from django.db import IntegrityError
from django.http import JsonResponse

from MyUser.views import createUser, login_access, getMyUserByUser, changeUser, deleteUserB, getUserByUsername
from Product.views import getProductById

# Create your views here.

def darkMode(request):
    DarkMode = request.POST.get("nightDaySlider") == 'on'
    print ('DarkMode', DarkMode)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    print (my_user)
    my_user.dark_mode = DarkMode
    my_user.save()
    return render(request, "users.html", context={'user': user, 'my_user': my_user})


def home(request):
    return render(request, "login.html")

def registerUser(request):
    return render(request, "register.html")

# def loginUser(request):
#     return render(request, "login.html")

def addUser(request):
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
    product = getProductById(6)
    print(product.photo)
    return render(request, "main.html", context={'user': user, 'my_user': my_user, 'product': product}) 

def user(request):
    #id = User.objects.get(id = iduser)
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "users.html", context={'user': user, 'my_user': my_user})

def editUser(request):
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "usersEdit.html", context={'user': user, 'my_user': my_user})

def modifyUser(request):
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

def deleteUser(request):
   deleteUserB(request.user.username)
   return redirect("home")
        

def myProducts (request):
    user = getUserByUsername(request.user.username)
    my_user = getMyUserByUser(user=user)
    return render(request, "myProducts.html", context={'user': user, 'my_user': my_user})

def addProduct(request):
    return render(request, "addProduct.html")
