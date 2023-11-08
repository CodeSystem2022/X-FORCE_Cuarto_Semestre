
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/product/', include('Product.urls')),
    path('test/shoppingcart/', include('ShoppingCart.urls')),
    path('test/purchases/', include('Purchases.urls'))
]
