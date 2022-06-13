from rest_framework import serializers
from farmacia.models import Comuna


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['idComuna','nomComuna','idREG']
        
        