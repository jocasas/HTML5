from xml.etree.ElementInclude import include
from django.urls import path,include
from.views import home,log,reg,catbell,catmasc,catmedi,catsexu,add,mod,delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('login/',log,name="log"),
    path('registro/',reg,name="reg"),
    path('categoriaBelleza/',catbell,name="catbell"),
    path('categoriaMascotas/',catmasc,name="catmasc"),
    path('categoriaSexualidad/',catsexu,name="catsexu"),
    path('categoriaMedicamentos/',catmedi,name="catmedi"),
    path('agregarProducto/',add,name="addProd"),
    path('mod/<id>',mod,name="mod"),
    path('delete/<id>',delete,name="delete"),
    path('API/',include('rest_Productos.urls')),
    path('API2/',include('rest_Direccion.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)