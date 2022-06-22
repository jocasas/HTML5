
from django.shortcuts import render, redirect

from farmacia.decorators import allowed_user, unauthenticated_user
from .models import Comuna,Region,Producto,Sucursal
from .forms import Tabla_agregar,SucursalForm,sucForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 

from django.contrib.auth.decorators import login_required


# Create your views here.
#======================================================================================
##VIEWS INDEX
    #componentes-en-la-funcion-def home():
    # view productos index
    # view sucursales index t/pc val,met
    # post django.form sucursales -- sucform

def home(request):
    productos = Producto.objects.all()
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    sucursalesVal = Sucursal.objects.filter(idComuna__in = [1,2,3])
    sucursalesMet = Sucursal.objects.filter(idComuna__in = [5,6,7])
    form = sucForm()
    if request.method=='POST':
            form = sucForm(request.POST)
            if form.is_valid():
                form.save()
    
    datos = {
        'productos':productos ,
        'sucursalesVal':sucursalesVal ,
        'sucursalesMet':sucursalesMet ,
        'region':region ,
        'comuna':comuna,
        'form':form
    }
    return render (request,'farmacia/index.html',datos)

def userPage(request):
    context = {}
    return render(request, 'farmacia/index2.html',context)
    
    #editar sucursal con django.forms
def editarSucursal(request, pk):
    
    suc = Sucursal.objects.get(numSucursal=pk)
    form = sucForm(instance=suc)
    
    if request.method == 'POST':
        form = sucForm(request.POST, instance=suc)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context = {'form':form}
    return render(request, 'farmacia/editarsucursal.html', context)
    
    
    # delete
def eliminarSucursal(request, codigo):
    numsuc = Sucursal.objects.get(numSucursal=codigo)
    numsuc.delete()
    
    return redirect('/')

#login django.user token.valid
def log(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request , username=username, password=password)

        
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password incorrect')

        
    context = {}    
    return render (request,'farmacia/sesion2.html',context)

def logoutUser(request):
    logout(request)
    return redirect('log')

#registro django.forms
@unauthenticated_user
def reg(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
        
            return redirect('log')

    context = {'form':form}
    return render (request,'farmacia/registro.html' ,context)

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
