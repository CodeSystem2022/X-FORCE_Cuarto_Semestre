from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

def getUserByUsername(username: int):
    try:
        user = get_object_or_404(User,username=username)
        return user
    except Exception as e:
        return e

def createUser(user):
    try:
        user = User.objects.create_user(username=user['username'], password=user['password'], email=user['email'])
        user.save()
        return True
    except Exception as e:
        return e
    
def login(username: str, password: str):
    try:
        user = authenticate(username=username, password=password)
        return user
    except Exception as e:
        return e