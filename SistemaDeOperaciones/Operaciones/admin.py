from django.contrib import admin
from .models import *
from Ventas.models import Venta

# Register your models here.

campos_de_solo_lectura = [
    'id_venta',
    'id_vivienda',
    # 'id_vendedor',
    'id_cliente',
    'id_banco',
    'forma_pago',
    'pie_abono_ven',
    'estado_ven',
    'fecha_ven',
    'monto_ven',
]

class OperacionesInline(admin.TabularInline):
    model = Operacione

# Añade la clase ModelAdmin si es necesario
class VentaOpAdmin(admin.ModelAdmin):
    inlines = [OperacionesInline,]
    # readonly_fields = campos_de_solo_lectura
    search_fields = ['id_venta']
    list_filter = ['id_venta', 'id_cliente']
    list_display = ['id_venta','id_vivienda', 'id_cliente','id_banco']



admin.site.register(CategoriaEtapa)
admin.site.register(Etapa)
admin.site.register(Operacione)
admin.site.register(VentaOp, VentaOpAdmin)
