from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'core/Index.html')

def Figuras(request):
    figuras = Producto.objects.all()
    return render(request, 'core/Figuras.html', {'figuras': figuras})

def accesorios(request):
    return render(request, 'core/accesorios.html')

def ropa(request):
    return render(request, 'core/ropa.html')

def login(request):
    return render(request, 'core/login.html')

