from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import os

# Create your views here.

def home(request):
    return render(request, "login.html")

def registerUser(request):
    return render(request, "register.html")

def main(request):
    return render(request, "main.html")

def user(request):
    #id = User.objects.get(id = iduser)
    return render(request, "users.html")
def editUser(request):
    return render (request, "usersEdit.html")
