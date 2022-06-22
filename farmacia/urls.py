from django.urls import path,include
from.views import home,log,reg,catbell,catmasc,catmedi,catsexu,add,mod,delete
from django.conf import settings
from django.conf.urls.static import static
from . import views

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)