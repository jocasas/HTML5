from tabnanny import verbose
from django.db import models
from datetime import datetime

# Create your models here.

class TipoProducto (models.Model):
    
    idTipo = models.IntegerField (primary_key= True, verbose_name= 'Tipo Producto')
    nombreTipo = models.CharField (max_length=50, verbose_name= 'Nombre Tipo')

    def __str__(self):
        return self.nombreTipo

class Producto (models.Model):

    idProducto = models.AutoField(primary_key=True, verbose_name='Id de Producto')
    photo_as_blob = models.ImageField(upload_to= 'farmacia/static/farmacia/img/imagenesDjango' ,verbose_name='imagen Producto')
    nombreProd = models.CharField(max_length=20, verbose_name='Nombre')
    descripEspecifica = models.CharField(max_length=200, verbose_name= 'Detalles')
    unidades = models.CharField (max_length=20, verbose_name= 'Unidad o medida')
    desc = models.TextField (max_length=500,null=True, blank=True ,verbose_name= 'descripcion')
    price = models.IntegerField (verbose_name='precio')
    stock = models.IntegerField (default=0, verbose_name='stock')
    IdTipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProd



# REGION -> COMUNA -> SUCURSAL
class Region (models.Model):
    
    idRegion = models.IntegerField(primary_key=True,verbose_name='Id de Region')
    nomRegion = models.CharField(max_length=40,verbose_name='Nombre region')
    
    def __str__(self):
        return self.nomRegion

class Comuna (models.Model):
    
    idComuna = models.IntegerField(primary_key=True,verbose_name='Id de Comuna')
    nomComuna = models.CharField(max_length=40,verbose_name='Nombre Comuna')
    IdRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomComuna

class Sucursal (models.Model):
    
    numSucursal = models.AutoField(primary_key=True, verbose_name='Numero Sucursal')
    Nombre = models.CharField(max_length=40, verbose_name='Nombre de la Sucursal')
    Direccion = models.CharField(max_length=60, verbose_name='Direccion')
    Horario= models.CharField(max_length=60, verbose_name='Abierto')
    idComuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)


    def __str__(self):
        return self.Nombre
    
class HistorialCompras (models.Model):
    
    idCompra = models.AutoField(primary_key=True,verbose_name='Codigo Compra')
    Usuario = models.CharField(max_length=200, verbose_name='Usuario')
    Productos = models.CharField(max_length=200, verbose_name='Productos Comprados')
    valTotal = models.IntegerField(verbose_name='Valor Total')
    fechaCompra = models.DateField(verbose_name='Fecha Compra')
    estado = models.CharField(max_length=50, verbose_name='Estado', default='Pendiente')
    fechallega = models.DateField(default=datetime.today)
    
    
    def __str__(self):
        return self.Usuario