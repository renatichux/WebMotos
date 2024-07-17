from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def info(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shopSingle(request):
    return render(request, 'shop-single.html')

def empleados(request):
   template = loader.get_template('empleados.html')
   return HttpResponse(template.render())   

def master(request):
    return render(request, 'master.html')

def login(request):
    return render(request, 'login.html')

def homeLogin(request):
    return render(request, 'home_login.html')


def sucursales(request):
   template = loader.get_template('sucursales.html')
   return HttpResponse(template.render())  

def cliente(request):
   template = loader.get_template('Clientes.html')
   return HttpResponse(template.render())

def productos(request):
   template = loader.get_template('productos.html')
   return HttpResponse(template.render())  

def cargo(request):
   template = loader.get_template('cargosEmpleados.html')
   return HttpResponse(template.render())  
# Create your views here.

# Create your views here.
