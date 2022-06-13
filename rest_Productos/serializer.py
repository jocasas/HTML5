from rest_framework import serializers
from farmacia.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto','photo_as_blob','nombreProd','descripEspecifica','unidades','desc','price','IdTipo']
        
        