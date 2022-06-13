from operator import methodcaller
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from farmacia.models import Sucursal
from rest_sucursales.serializer import SucursalSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_sucursales(request):
    if request.method == 'GET':
        listaSucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(listaSucursales, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataS = JSONParser().parse(request)
        serializer = SucursalSerializer(data = dataS)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def detalle_sucursal(request,id):
    try:
        sucursal = Sucursal.objects.get(numSucursal=id)
    except sucursal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SucursalSerializer(sucursal)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataS = JSONParser().parse(request)
        serializer = SucursalSerializer(data = dataS)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        sucursal.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
