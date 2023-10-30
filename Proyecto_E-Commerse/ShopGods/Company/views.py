from Company.models import Company
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


def getCompanyById(id: int):
    try:
        company = get_object_or_404(Company,id=id)
        return company
    except Exception as e:
        return e
    
def getCompanies(amount: int = None, search: str = None):
    try:
        if search:
            condition = Q(name__icontains=search)
            if amount:
                return Company.objects.filter(condition)[:amount]
            else:
                return Company.objects.filter(condition)

        if not search:
            if amount:
                return Company.objects.filter()[:amount]
            else:
                return Company.objects.filter()
    except Exception as e:
        return e
        
# Facu - Funcion que permita crear una compania
def createCompany(company):
    # Crear una nueva persona
    # persona = Persona(nombre="Juan", apellido="Pérez", edad=25)
    # persona.save()
    return

def createCompanies(companies):
    try:
        Company.objects.bulk_create(companies)
        return True
    except Exception as e:
        return e

def updateCompany(id, company):
    
    return

# Cristian - Funcion que borra una fila por id
def deleteCompanyById(id: int):
    return

def test(request):
    companie = getCompanyById(6)
    print(f'Error -> {type(companie)}')
    if type(companie) is Http404:
        print("El error es 404")
    return HttpResponse('Hola')

