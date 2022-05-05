from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'farmacia/index.html')
def log(request):
    return render (request,'farmacia/sesion2.html')
def reg(request):
    return render (request,'farmacia/registro.html')
def catbell(request):
    return render (request,'farmacia/belleza.html')
def catmasc(request):
    return render (request,'farmacia/mascotas.html')
def catsexu(request):
    return render (request,'farmacia/sexualidad.html')
def catmedi(request):
    return render (request,'farmacia/medicamentos.html')
