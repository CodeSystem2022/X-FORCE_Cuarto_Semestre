from Company.models import Company
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404


def getCompanyById(id: int):
    try:
        company = get_object_or_404(Company,id=id)
        return company
    except Exception:
        return None
    
def getCompanies(amount: int = None, search: str = None):
    print('Hola')
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
            print('ACA 1')
            return Company.objects.filter()
        
# Facu - Funcion que permita crear una compania
def createCompany(company):
    # Crear una nueva persona
    # persona = Persona(nombre="Juan", apellido="Pérez", edad=25)
    # persona.save()
    return

def createCompanies():
    return

def updateCompany(company: Company):
    return

# Cristian - Funcion que borra una fila por id
def deleteCompanyById(id: int):
    try:
        fila = get_object_or_404(Company, id=Id)
        fila.delete()
        return True
    except Company.e:
        return False



def test(request):
    companies = getCompanies()
    print(companies)
    return HttpResponse('Hola')

