from rest_framework import serializers
from farmacia.models import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['numSucursal','Nombre','Direccion','Horario','idComuna']
        
        