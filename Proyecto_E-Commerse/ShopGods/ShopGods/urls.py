
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/company/', include('Company.urls')),
    path('test/product/', include('Product.urls'))
    
]
