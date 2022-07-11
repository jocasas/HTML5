from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

from .models import Producto, Sucursal

#Este proceso se repite por cada formulario
class Tabla_agregar(ModelForm):
    class Meta:
        model = Producto
        #Aqui van los campos que se rellenan (los incrementales no)
        fields = ['nombreProd','photo_as_blob','descripEspecifica','unidades','desc','price','stock','IdTipo']
        
class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['numSucursal','Nombre','Direccion','Horario','idComuna']
        
class sucForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        