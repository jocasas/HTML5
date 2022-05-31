from django import forms
from django.forms import ModelForm
from .models import Producto

#Este proceso se repite por cada formulario
class Tabla_agregar(ModelForm):
    class Meta:
        model = Producto
        #Aqui van los campos que se rellenan (los incrementales no)
        fields = ['nombreProd','photo_as_blob','descripEspecifica','unidades','desc','price','IdTipo']