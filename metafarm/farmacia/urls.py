from django.urls import path
from.views import home,log,reg,catbell,catmasc,catmedi,catsexu 

urlpatterns = [
    path('',home,name="home"),
    path('login/',log,name="log"),
    path('registro/',reg,name="reg"),
    path('categoriaBelleza/',catbell,name="catbell"),
    path('categoriaMascotas/',catmasc,name="catmasc"),
    path('categoriaSexualidad/',catsexu,name="catsexu"),
    path('categoriaMedicamentos/',catmedi,name="catmedi"),
    
]