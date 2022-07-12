from django.shortcuts import render, redirect
from farmacia.cart import Carrito

from datetime import datetime, timedelta
from farmacia.decorators import unauthenticated_user
from .models import Comuna, HistorialCompras,Region,Producto,Sucursal
from .forms import Tabla_agregar,sucForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
import random


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

#======================================================================================
# MODIFICAR SUCURSAL CON MODELS Y FORMS
    
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
    
 #======================================================================================
# ELIMINAR SUCURSAL CON MODELS
   
    # delete
def eliminarSucursal(request, codigo):
    numsuc = Sucursal.objects.get(numSucursal=codigo)
    numsuc.delete()
    
    return redirect('/')

#======================================================================================
# LOGIN DEF


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
            messages.info(request,'Usuario o Contraseña Incorrecta')

        
    context = {}    
    return render (request,'farmacia/sesion2.html',context)

#======================================================================================
# DEF LOGOUT


def logoutUser(request):
    logout(request)
    return redirect('log')

#======================================================================================
# REGISTRO USUARIOS DJANGO

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
#VIEWS COMPRAS
def comp(request):
    productos = Producto.objects.all()
    datos = {
        'productos':productos
    }
    
    return render (request,'farmacia/compras.html',datos)
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
    return redirect(request.META['HTTP_REFERER'])

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

#======================================================================================
# AGREGAR A CARRITO
def add_carrito (request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(idProducto = producto_id)
    carrito.agregar(productos)
    messages.success(request,"agregado correctamente")
    return redirect(request.META['HTTP_REFERER'])

#======================================================================================
# ELIMINAR DE CARRITO

def del_carrito (request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(idProducto = producto_id)
    carrito.eliminar(productos)
    return redirect ('comp')

#======================================================================================
# RESTAR DE CARRITO

def rest_carrito (request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(idProducto = producto_id)
    carrito.restar(productos)
    return redirect ('comp')

#======================================================================================
# LIMPIAR CARRITO

def cln_carrito (request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect ('comp')


""" def comprar (request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(idProducto = producto_id)
    carrito.comprar(productos)
    productos.save()
    return redirect(to='home') """
    
#======================================================================================
# RESTAR STOCK INTERACCION CARRITO

def restar_stock(cantidad,prod_id):
    Productos = Producto.objects.get(idProducto = prod_id)
    Productos.stock -= cantidad
    Productos.save()


''' def comprar (request):
    carrito = Carrito(request)
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            restar_stock(int(value["cantidad"]),int(value["producto_id"]))
            carrito.limpiar()
    return redirect ('home')
 '''
#======================================================================================
# COMPRAR --> SAVE HISTORIAL MODELS.MODEL


def comprar (request):
    carrito = Carrito(request)
    producto = ''
    valor = 0 
    
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            restar_stock(int(value["cantidad"]),int(value["producto_id"]))
            producto = producto + str(value["cantidad"])+ ' - ' +  value["nombre"] + ': ' + value["descripcion"] + ' , '
            valor = valor + value["acumulado"]
            username = request.user.username

        # numero al azar (suponiendo de uno a siete dias habiles) -jose
        pluseven = random.randint(1,7)
        plusfecha = datetime.today()
        despa = plusfecha + timedelta(days=pluseven)

                    # historial se llena con la fecha actual y la fecha actual + random(number)
        HistorialCompras.objects.create(
            Usuario = username,
            Productos = producto,
            valTotal = valor,
            fechaCompra=datetime.today(),
            fechallega=despa
        )

        ''' fechaDespacho= despa '''
        ''' 
        tag= 0
        while HistorialCompras.objects.filter(idCompra=tag).exist():   
            HistorialCompras.objects.create(
                idCompra = tag + 1,
                Usuario = username,
                Productos = producto,
                valTotal = valor,
                fechaCompra=datetime.datetime.now()
            ) '''
        

    carrito.limpiar()
    return redirect ('his')

#======================================================================================
# RENDER HISTORIAL USUARIO NORMAL


def Historial (request):
    username = request.user.username
    historial = HistorialCompras.objects.filter(Usuario=username)
    context = {
        'com':historial
    }
    return render(request,'farmacia/historial.html',context) 

#======================================================================================
# RENDER HISTORIAL DE TODOS LOS USUARIOS PARA USUARIO STAFF


def HistorialAdmin (request):
    historial = HistorialCompras.objects.all()
    context = {
        'com':historial
    }
    return render(request,'farmacia/historialadm.html',context)


#======================================================================================
# ACTUALIZANDO ESTADO DE HISTORIAL POR FECHA [ordenado,recibido]-> PEDIDO (?) boleta (?) nose -jose
# nos falta hablar del lugar donde esta supongo -jose 

def HistorialEstadoUpdate (self,nbol):
    historial = HistorialCompras.objects.get(idCompra=nbol)
    hoy = datetime.today().date()
    fechallega = historial.fechallega
    if hoy >= fechallega:
        historial.estado = 'Recibido'
        historial.save()
         
    return redirect('hisadm')

#wip no tocar 

#======================================================================================
# a no se -jose
# if apreta un boton ?

def estadoDespacho(request,idCompra):
    despacho = HistorialCompras.objects.filter(idCompra=idCompra)
    datos= {'despacho':despacho}
    return render(request,'farmacia/estadoDespacho.html',datos)


#======================================================================================
# Editar Estado
# Pendiente
def editarEstadoManual1(self, nbol):
    
    histo = HistorialCompras.objects.get(idCompra=nbol)
    print('Estado Anterior: '+ histo.estado)
    histo.estado = 'Pendiente'
    print('Estado Nuevo:' + histo.estado)
    histo.save()
    
    return redirect('hisadm')
           
# Cancelado 
def editarEstadoManual2(self, nbol):
    
    histo = HistorialCompras.objects.get(idCompra=nbol)
    print('Estado Anterior: '+ histo.estado)
    histo.estado = 'Cancelado'
    print('Estado Nuevo:' + histo.estado)
    histo.save()
    
    return redirect('hisadm')

# En camino 
def editarEstadoManual3(self, nbol):
    
    histo = HistorialCompras.objects.get(idCompra=nbol)
    histo.estado = 'En Camino'
    histo.save()
    
    return redirect('hisadm')

# Recibido 
def editarEstadoManual4(self, nbol):
    
    histo = HistorialCompras.objects.get(idCompra=nbol)
    histo.estado = 'Recibido'
    histo.save()
    
    return redirect('hisadm')
            