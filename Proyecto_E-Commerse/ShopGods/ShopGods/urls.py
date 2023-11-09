
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
    path("User/",views.user, name="user"),

#--------------------Referido a Productos----------------------------------------------#

    path("MyProducts/", views.myProducts, name="myProducts"),
    path("addProduct/", views.addProduct, name="addProduct"),
    path("createProductF/", views.createProductF, name="createProductF"),
    path("updateProductF/", views.updateProductF, name="updateProductF"),
    path("myProductEdit/<int:id_product>/", views.myProductEdit, name="myProductEdit"),
    path("product/<int:id_product>/", views.product, name="product"),
    path("deleteProduct/<int:id_product>/", views.deleteProduct, name="deleteProduct"),

#--------------------Referido a carrito de compras----------------------------------------------#


    path("MyShopCart/", views.myShopCart, name="myShopCart"),
 #   path("addShopCart/", views.addShopCart, name="addShopCart"),
 #   path("deleteShopCart/", views.deleteShopCart, name="deleteShopCart"),
 #   path("payShopCart/", views.payShopCart, name="payShopCart"),



    path("Main/", views.main, name="main"),



#--------------------Otros programas----------------------------------------------#    
    path('darkMode/', views.darkMode, name='darkMode'),

#----------Rutas de la aplicación----------#
    path('login/', include('Core.urls')),

    path('test/product/', include('Product.urls')),
]
