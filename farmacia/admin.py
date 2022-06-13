from django.contrib import admin
from .models import TipoProducto, Producto, Region, Comuna, Sucursal
from django.utils.html import format_html

# Register your models here.
class PersonAdmin (admin.ModelAdmin):

    list_display = (
        'idProducto',
        'nombreProd',
        'IdTipo',
        'imgen',
        
    )
    #
    search_fields = ['nombreProd',]
    list_filter = ('IdTipo',)
    #

    def imgen(self, obj):
        return format_html('<img src={} width="130" height="100" />', obj.photo_as_blob.url)

admin.site.register(TipoProducto)
admin.site.register(Producto, PersonAdmin)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sucursal)
