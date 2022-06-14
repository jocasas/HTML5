from optparse import check_choice
from django.shortcuts import render 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    dausername = data['username']
    dapassword = data['password']
    try:
        usuario = User.objects.get(username = dausername)
    except User.DoesNotExist:
        return Response("Usuario Invalido")
    
    pass_valido = check_password(dapassword, usuario.password)
    if not pass_valido:
        return Response("Password Incorrecta")
    
    token, created = Token.objects.get_or_create(user=usuario)
    return Response(token.key)

    