from django.shortcuts import render
from .models import CentralOffice, Branch, Client, Account

def index(request):
    return render(request, 'core/index.html')

def central_offices(request):
    offices = CentralOffice.objects.all()
    return render(request, 'core/central_offices.html', {'offices': offices})

def branches(request):
    branches = Branch.objects.all()
    return render(request, 'core/branches.html', {'branches': branches})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'core/clients.html', {'clients': clients})

def accounts(request):
    accounts = Account.objects.all()
    return render(request, 'core/accounts.html', {'accounts': accounts})
