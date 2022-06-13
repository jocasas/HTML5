from re import I
from django.urls import URLPattern, path
from rest_Direccion.views import lista_comunas,detalle_comuna

urlpatterns = [
    path('lista_comunas',lista_comunas,name="lista_comunas"),
    path('detalle_comuna/<id>',detalle_comuna,name="detalle_comuna"),
]


