
from django.shortcuts import render, redirect
from .models import Comuna,Region,Producto,Sucursal
from .forms import Tabla_agregar
from django.contrib import messages





# Create your views here.
#======================================================================================
##VIEWS INDEX
def home(request):
    productos = Producto.objects.all()
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    sucursalesVal = Sucursal.objects.filter(idComuna__in = [1,2,3])
    sucursalesMet = Sucursal.objects.filter(idComuna__in = [5,6,7])
    
    datos = {
        'productos':productos ,
        'sucursalesVal':sucursalesVal ,
        'sucursalesMet':sucursalesMet ,
        'region':region ,
        'comuna':comuna
    }
    return render (request,'farmacia/index.html',datos)
def log(request):
    return render (request,'farmacia/sesion2.html')
def reg(request):
    return render (request,'farmacia/registro.html')

#======================================================================================
##VIEWS BELLEZA
def catbell(request):
    productos = Producto.objects.filter(IdTipo = 3)
    datos = {
        'productos':productos
    }

    return render (request,'farmacia/belleza.html',datos)

#======================================================================================
##VIEWS MASCOTAS
def catmasc(request):
    productos = Producto.objects.filter(IdTipo = 0)
    datos = {
        'productos':productos
    }
    
    return render (request,'farmacia/mascotas.html',datos)

#======================================================================================
##VIEWS SEXUALIDAD
def catsexu(request):
    productos = Producto.objects.filter(IdTipo = 2)
    datos = {
        'productos':productos
    }
    

    return render (request,'farmacia/sexualidad.html',datos)

#======================================================================================
#VIEWS MEDICAMENTOS
def catmedi(request):
    productos = Producto.objects.filter(IdTipo = 1)
    datos = {
        'productos':productos
    }
    
    return render (request,'farmacia/medicamentos.html',datos)
#======================================================================================
#MODIFICAR
def mod (request, id):
    productos = Producto.objects.get(idProducto = id)
    datos = {
        'Agregar':Tabla_agregar(instance= productos)
    }
    if(request.method == 'POST'):
        varModificar = Tabla_agregar(request.POST, request.FILES ,instance=productos)
        if varModificar.is_valid():
            varModificar.save()
            messages.success(request,"modificado correctamente")
        return redirect(to='home')
    return render (request,'farmacia/update.html',datos)
    
#======================================================================================
#ELIMINAR

def delete (request,id):
    messages.success(request,"eliminado correctamente")
    productos = Producto.objects.get(idProducto = id)
    productos.delete()
    return redirect(to='home')

#======================================================================================
#AGREGAR FOTO MEDIANTE FORMULARIO
def add(request):
    #Mostrar el formulario del form al html
    datos = {'Agregar':Tabla_agregar()}
    if (request.method == 'POST'):
    #rescatar la invormacion
        varFomulario = Tabla_agregar(request.POST,request.FILES)
        if varFomulario.is_valid():
            varFomulario.save() #insert a la base de datos
        else: 
            #mensaje de error
            datos['error'] = 'Producto NO guardado'

    return render(request,'farmacia/agregarProd.html',datos)

#AGREGAR SUCUR(?)
