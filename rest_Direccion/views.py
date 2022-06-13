from operator import methodcaller
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from farmacia.models import Comuna
from rest_Direccion.serializer import ComunaSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_comunas(request):
    if request.method == 'GET':
        listaComunas = Comuna.objects.all()
        serializer = ComunaSerializer(listaComunas, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataC = JSONParser().parse(request)
        serializer = ComunaSerializer(data = dataC)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def detalle_comuna(request, id):
    try:
        comuna = Comuna.objects.get(idComuna = id)
    except comuna.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ComunaSerializer(comuna)
        return Response(serializer.data)
    elif request.method == "PUT":
        dataC = JSONParser().parse(request)
        serializer = ComunaSerializer(Comuna, data = dataC)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        comuna.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    