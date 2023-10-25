from Company.models import Company
from django.http import HttpResponse

def getCompany(value: int | str, colum_name: str = 'both'):
    return colum_name

def getCompanies(amount: int = None, search: any = None): # denifinir parametros de filtros
    return

def createCompany(company: Company):
    return

def createCompanies():
    return

def updateCompany(company: Company):
    return

def deleteCompany():
    return

def test(request):
    print(getCompany(12))
    return HttpResponse("Hola mundo")