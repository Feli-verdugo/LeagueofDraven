from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'core/Index.html')

def Figuras(request):
    figuras = Producto.objects.all()
    return render(request, 'core/Figuras.html', {'figuras':figuras, "carro":request.session.get("carro", [])})

def accesorios(request):
    return render(request, 'core/accesorios.html')

def ropa(request):
    return render(request, 'core/ropa.html')

def login(request):
    return render(request, 'core/login.html')

def carrito(request):
    return render(request, 'core/carrodos.html', {"carro":request.session.get("carro", [])})

def dropitem(request, id):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect (to="carrito")

def addtocar(request, id):
    producto = Producto.objects.get(id=id)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == id:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([id, producto.nombre, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect (to="figuras")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")   
