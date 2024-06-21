from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    precio = models.IntegerField(null=False)
    url_imagen = models.CharField(max_length=400,null=False)