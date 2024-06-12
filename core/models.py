from django.db import models

class Producto(models.Model):
    id = models.CharField(max_length=4,primary_key= True)
    nombre = models.CharField(max_length= 200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=255)


