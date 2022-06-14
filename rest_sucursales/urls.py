from django.urls import URLPattern, path
from rest_sucursales.views import lista_sucursales, detalle_sucursal
from rest_sucursales.viewsLogin import login

urlpatterns = [
    path('lista_sucursales',lista_sucursales,name="lista_sucursales"),
    path('detalle_sucursal/<id>',detalle_sucursal,name="detalle_sucursal"),
    path('login',login, name="login"),
]
