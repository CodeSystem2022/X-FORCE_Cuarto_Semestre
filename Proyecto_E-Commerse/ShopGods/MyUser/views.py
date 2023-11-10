from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .models import MyUser


def getUserByUsername(username: str):
    try:
        user = get_object_or_404(User, username=username)
        return user
    except Exception as e:
        return e


def createUser(user):
    try:
        user = User.objects.create_user(
            username=user['username'], password=user['password'], email=user['email'])
        user.save()
        myUser = MyUser(user=user)
        myUser.save()
        return user
    except Exception as e:
        print('Entra a exepcion', e)
        return e


def login_access(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return user
    else:
        return None


def changeToDarckMode():
    return


def getMyUserByUser(user):
    try:
        myUser = MyUser.objects.get(user=user)
        return myUser
    except Exception as e:
        return None


def changeUser(username: str = None, old_username: str = None, password: str = None, email: str = None, cbu: int = 0, profile_photo: str = None):
    try:
        user = getUserByUsername(username=old_username)
        user.username = username
        user.email = email
        if password:
            user.set_password(password)
        user.save()
        print('ACa1')
        myUser = getMyUserByUser(user)
        print('myUser', myUser)
        print('Aca 2')
        myUser.cbu = cbu if cbu.isnumeric() else 0
        myUser.profile_photo = profile_photo
        myUser.save()
        return list(user, myUser)
    except Exception as e:
        return e


def deleteUserB(username):
    try:
        User.objects.get(username=username).delete()
        return True
    except Exception as e:
        return e

# def login(username: str, password: str):
#     try:
#         UserList = User.objects.all()
#         users = list(set(UserList.values_list('username', 'password')))

#         inputList = [username, password]

#         print(users)
#         print(inputList)

#         for index in users:
#             print (index, "\n", inputList)
#             if index[0] == inputList[0] and index[1] == inputList[1]:
#                 return True

#         return False
#     except Exception as e:
#         return e
