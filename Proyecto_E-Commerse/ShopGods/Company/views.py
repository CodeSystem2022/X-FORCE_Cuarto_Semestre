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
        

def createCompany(company_param):
    try:
        company = Company(name=company_param["name"]) 
        company.save()
        return True
    except Exception as e:
        return e     
         
def createCompanies(companies):
    try:
        company_list = []
        for company in companies:
            company_list.append(Company(name=company["name"]))
        Company.objects.bulk_create(company_list)
        return True
    except Exception as e:
        return e

def updateCompany(id, company_param):
    try:
        company = getCompanyById(id)
        company.name = company_param["name"]
        company.save()
        return True
    except Exception as e:
        return e

def deleteCompanyById(id: int):
    try:
        company = getCompanyById(id)
        company.delete()
        return True
    except Exception as e:
        return e

def test(request):
    response = updateCompany(3,{'name':'Fravega'})
    print(type(response))
    if response is True:
        print('La respuesta es verdadera')
    elif isinstance(response, AttributeError):
        print('Error AttributeError')
    elif isinstance(response, Exception):
        print('No se pudo crear la compania')
        
    print('Se finalizo la prueba')
    return HttpResponse('Esta funcionando correctamento')

