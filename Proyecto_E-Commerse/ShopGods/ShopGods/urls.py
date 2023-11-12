
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from Core import views


urlpatterns = [
    # -----------------------------Login---------------------------------------------------#
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('loginF/', views.loginF, name='loginF'),
    
     path("reset_password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
     path("reset_password_send/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
     path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
     path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),


    # --------------------Referido a Usuarios----------------------------------------------#
    path("registerUser/", views.registerUser, name="registerUser"),
    path("modifyUser/", views.modifyUser, name="modifyUser"),
    path("editUser/", login_required(views.editUser), name="editUser"),
    path('addUser/', views.addUser, name='addUser'),
    path("deleteUser/", views.deleteUser, name="deleteUser"),
    path("user/<int:int_null>", login_required(views.user), name="user"),

    # --------------------Referido a Productos----------------------------------------------#

    path("MyProducts/", login_required(views.myProducts), name="myProducts"),
    path("addProduct/", views.addProduct, name="addProduct"),
    path("createProductF/", views.createProductF, name="createProductF"),
    path("updateProductF/", views.updateProductF, name="updateProductF"),
    path("myProductEdit/<int:id_product>/",
         views.myProductEdit, name="myProductEdit"),
    path("product/<int:id_product>/", views.product, name="product"),
    path("deleteProduct/<int:id_product>/",
         views.deleteProduct, name="deleteProduct"),

    path("createItem/", views.createItem, name="createItem"),
    path("deleteItem/<int:id_item>/<int:id_product>/<str:product_type>/",
         views.deleteItem, name="deleteItem"),

    # --------------------Referido a carrito de compras----------------------------------------------#


    path("MyShopCart/", views.myShopCart, name="myShopCart"),
    path("addProductToShoppingCartF/<int:id_product>/",
         views.addProductToShoppingCartF, name="addProductToShoppingCartF"),
    path("deleteShopCart/<int:id_shopcart>/",
         views.deleteShopCart, name="deleteShopCart"),
    path("payShopCart/<int:id_shopping_cart>/",
         views.payShopCart, name="payShopCart"),
    path("pago/",
         views.pago, name="pago"),


    path("Main/", views.main, name="main"),



    # --------------------Referido a carrito de compras----------------------------------------------#


    path("MyRecord/",  login_required(views.myRecord), name="myRecord"),
    path("Historybuy/<int:id_record>",
         login_required(views.historyBuy), name="historyBuy"),
    #    path("Historybuy/<int:id_user>", views.Historybuy, name="Historybuy"),




    # --------------------Otros programas----------------------------------------------#
    path('darkMode/', views.darkMode, name='darkMode'),

    path('formNull/<int:int_null>', views.formNull, name='formNull'),

    # ----------Rutas de la aplicación----------#
    path('login/', include('Core.urls')),

    path('test/product/', include('Product.urls')),
]
