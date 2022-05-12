from django.db import models

# Create your models here.

class TipoProducto (models.Model):
    
    idTipo = models.IntegerField (primary_key= True, verbose_name= 'Tipo Producto')
    nombreTipo = models.CharField (max_length=50, verbose_name= 'Nombre Tipo')

    def __str__(self):
        return self.nombreTipo

class Producto (models.Model):

    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    photo_as_blob = models.ImageField(upload_to= 'farmacia/static/farmacia/img/imagenesDjango' ,verbose_name='imagen Producto')
    nombreProd = models.CharField(max_length=20, verbose_name='Nombre Producto')
    descripEspecifica = models.CharField(max_length=200, verbose_name= 'DescripEspecifica')
    unidades = models.CharField (max_length=20, verbose_name= 'Unidades')
    desc = models.CharField (max_length=500,null=True, blank=True ,verbose_name= 'descripcion')
    price = models.IntegerField (verbose_name='precio')
    IdTipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProd
