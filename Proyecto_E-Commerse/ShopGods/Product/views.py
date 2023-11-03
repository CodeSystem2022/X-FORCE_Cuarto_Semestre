from .models import Product
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.db.models.query import QuerySet


def getProductById(id: int):
    try:
        product = get_object_or_404(Product,id=id)
        return product
    except Exception as e:
        return e
    
    
def getProducts(amount_per_page: int = 25, actual_page: int = 1, search: str = None, filter: any = None):
    try:
        condition = Q(name__icontains=search) & Q(company__in=filter['companies']) if filter["companies"] else Q(name__icontains=search)


        products = Product.objects.filter(condition)[(amount_per_page*actual_page)-amount_per_page:amount_per_page*actual_page]
        return products
    
    except Exception as e:
        return e


def test(request):
    response = getProducts(amount_per_page=10, actual_page=1, search="", filter={"companies": [2,3,5]})
    
    print(type(response))
    if isinstance(response, QuerySet):
        print(response)
    elif isinstance(response, AttributeError):
        print('Error AttributeError')
    elif isinstance(response, Exception):
        print('No se pudo crear la compania')
        
    print('Se finalizo la prueba')
    return HttpResponse('Esta funcionando correctamento')

        
    
    
    
    
    
    
    
    
    
    

    
# def getProducts(amount: int = None, search: str = None, filters: any = None):
#     try:
#         if search:
#             condition = Q(name__icontains=search)
#             if amount:
#                 return Product.objects.filter(condition)[:amount]
#             else:
#                 return Product.objects.filter(condition)

#         if not search:
#             if amount:
#                 return Product.objects.filter()[:amount]
#             else:
#                 return Product.objects.filter()
#     except Exception as e:
#         return e










