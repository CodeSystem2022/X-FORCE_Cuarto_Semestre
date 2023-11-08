
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from Core import views

urlpatterns = [
#-----------------------------Login---------------------------------------------------#
    path('admin/', admin.site.urls),
    path("", LoginView.as_view(template_name='login.html'), name="login"),
    path('loginF/', views.loginF, name='loginF'),

#--------------------Referido a Usuarios----------------------------------------------#
    path("RegisterUser/", views.registerUser, name="registerUser"),
    path("modifyUser/", views.modifyUser, name="modifyUser"),
    path("EditUser/", views.editUser, name="editUser"),
    path('addUser/', views.addUser, name='addUser'),
    path("deleteUser/", views.deleteUser, name="deleteUser"),


#--------------------Referido a Productos----------------------------------------------#

    path("MyProducts/", views.myProducts, name="myProducts"),
    path("addProduct/", views.addProduct, name="addProduct"),
    #path("MyProductsRegister/", views.MyProductsRegister, name="MyProductsRegister"),




    path("Main/", views.main, name="main"),
    path("User/",views.user, name="user"),


#--------------------Otros programas----------------------------------------------#    
    path('darkMode/', views.darkMode, name='darkMode'),

#----------Rutas de la aplicación----------#
    path('login/', include('Core.urls')),

    path('test/product/', include('Product.urls')),
]
