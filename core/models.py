from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()


    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:16]




class Producto(models.Model):
    id = models.CharField(max_length=4,primary_key= True)
    nombre = models.CharField(max_length= 200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)
    categoria = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre+" ("+self.id+")"
    

class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    

    def __str__(self):
        return str(self.id)+" "+self.producto.nombre[0:20]+" "+str(self.venta.id)