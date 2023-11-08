
from django.contrib import admin
from django.urls import path, include
from Core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="login"),
    path("RegisterUser/", views.registerUser, name="registerUser"),

    path("Main/", views.main, name="main"),

    path("User/",views.user, name="user"),
    path("EditUser/", views.editUser, name="editUser"),


#----------Rutas de la aplicación----------#
    path('login/', include('Core.urls')),

    path('test/product/', include('Product.urls')),
]
