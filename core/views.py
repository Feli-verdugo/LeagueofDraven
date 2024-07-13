from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse


def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    
    carro = request.session.get("carro", [])
    if not carro:
        return redirect(to="carrito")

    total = sum(item[5] for item in carro)
    
    venta = Venta(cliente=request.user, total=total)
    venta.save()
    
    for item in carro:
        producto = Producto.objects.get(id=item[0])
        
        if producto.stock >= item[4]:
            producto.stock -= item[4]
            producto.save()
            
            detalle = DetalleVenta(
                producto=producto,
                precio=item[3],
                cantidad=item[4],
                venta=venta
            )
            detalle.save()
        else:
            
            
            return HttpResponse(f'No hay suficiente stock disponible para {producto.nombre}.')
    
    request.session["carro"] = []
    return redirect(to="carrito")



def home(request):
    return render(request, 'core/Index.html')

def Figuras(request):
    figuras = Producto.objects.filter(categoria="FIGURA")
    return render(request, 'core/Figuras.html', {'figuras':figuras, "carro":request.session.get("carro", [])})

def accesorios(request):
    accesorios = Producto.objects.filter(categoria="ACCESORIOS")
    return render(request, 'core/accesorios.html', {'accesorios':accesorios, "carro":request.session.get("carro", [])})

def ropa(request):
    ropa = Producto.objects.filter(categoria="ROPA")
    return render(request, 'core/ropa.html', {'ropas':ropa, "carro":request.session.get("carro", [])})

def login(request):
    return render(request, 'core/login.html')

def carrito(request):
    carro = request.session.get("carro", [])
    total = sum(item[5] for item in carro)  # Calcula el total del carrito
    return render(request, 'core/carrodos.html', {"carro": carro, "total": total})

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
    return redirect (to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")   


def registro(request):
    if request.method == 'POST':
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html',{'form':registro})


