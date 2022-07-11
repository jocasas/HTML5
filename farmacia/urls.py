from django.urls import path,include
from.views import Historial,HistorialAdmin,HistorialEstadoUpdate, add_carrito, cln_carrito, comprar, del_carrito, estadoDespacho, home,log,reg,catbell,catmasc,catmedi,catsexu,add,mod,delete,comp, rest_carrito
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home,name="home"),
    path('login/',views.log,name="log"),
    path('logout/',views.logoutUser,name="logout"),
    path('registro/',views.reg,name="reg"),
    path('categoriaBelleza/',catbell,name="catbell"),
    path('categoriaMascotas/',catmasc,name="catmasc"),
    path('categoriaSexualidad/',catsexu,name="catsexu"),
    path('categoriaMedicamentos/',catmedi,name="catmedi"),
    path('agregarProducto/',add,name="addProd"),
    path('mod/<id>',mod,name="mod"),
    path('delete/<id>',delete,name="delete"),
    path('API/', include('rest_sucursales.urls')),
    path('eliminarSucursal/<codigo>',views.eliminarSucursal),
    path('editarSucursal/<str:pk>/',views.editarSucursal, name="update"),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('Compra/', comp, name="comp"),
    path('agregar/<int:producto_id>', add_carrito, name="add"),
    path('eliminar/<int:producto_id>', del_carrito, name="del"),
    path('restar/<int:producto_id>', rest_carrito, name="rest"),
    path('comprar/', comprar, name="comprar"),
    path('limpiar/', cln_carrito, name="cln"),
    path('historial/',Historial,name="his"),
    path('historialadm/',HistorialAdmin,name="hisadm"),
    path('historial/<nbol>',HistorialEstadoUpdate,name="changestate"),
    path('estadoDespacho/<idCompra>',estadoDespacho,name="des"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)