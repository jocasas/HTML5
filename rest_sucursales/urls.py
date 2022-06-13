from django.urls import URLPattern, path
from rest_sucursales.views import lista_sucursales,detalle_sucursal

urlpatterns = [
    path('lista_sucursales',lista_sucursales,name="lista_sucursales"),
    path('detalle_sucursal/<id>',detalle_sucursal,name="detalle_sucursal"),
]
