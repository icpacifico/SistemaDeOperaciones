from django.contrib import admin
from .models import *
# admin.py

from django.contrib import admin
from .models import (
    Profile, Nacionalidad, Banco, Uf, ConjuntoParametros,
    Profesion, Comisione, Parametros_Comisione
)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')

class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('id_nacionalidad', 'nombre_nacionalidad')
    search_fields = ('nombre_nacionalidad',)

class BancoAdmin(admin.ModelAdmin):
    list_display = ('id_banco', 'nombre_banco')
    search_fields = ('nombre_banco',)

class UfAdmin(admin.ModelAdmin):
    list_display = ('id_registro', 'valor_uf', 'fecha_registro')
    search_fields = ('fecha_registro',)
    list_filter = ('fecha_registro',)

class ConjuntoParametrosAdmin(admin.ModelAdmin):
    list_display = (
        'id_conjunto_parametros', 'id_condominio', 'factor_vendedor',
        'precio_dcto_depto', 'bono_precio_porce', 'porcen_promesa',
        'porcen_escritura', 'porcen_comision_vendedor', 'monto_escrt_operaciones',
        'monto_reserva', 'monto_prorrateo', 'monto_recuperar', 'fecha_recuperacion',
        'valor_bodega', 'valor_estacionamiento', 'fecha_termino_venta',
        'direccion_condominio', 'banco_alzante'
    )
    search_fields = ('id_condominio__nombre_condominio',)
    list_filter = ('fecha_recuperacion', 'fecha_termino_venta', 'banco_alzante')

class ComisioneAdmin(admin.ModelAdmin):
    list_display = (
        'id_comision', 'id_venta', 'id_asesor', 'id_cliente', 'fecha_registro',
        'fecha_promesa', 'fecha_escritura', 'fecha_desistimiento', 'valor_uf',
        'concepto', 'proyecto', 'etapa', 'unidad', 'bono_precio', 'monto_venta',
        'porcentaje_comision', 'comision_uf', 'comision_promesa_uf',
        'comision_promesa_clp', 'comision_escritura_uf', 'comision_escritura_clp',
        'bono_precio_uf', 'bono_precio_promesa_uf', 'bono_precio_promesa_clp',
        'bono_precio_escritura_uf', 'bono_precio_escritura_clp', 'monto_bono_c1',
        'monto_bono_c2', 'monto_bono_c3', 'monto_desistimiento', 'total_comisiones',
        'saldo_pagar', 'total_bonos', 'total_bonos_comisiones'
    )
    search_fields = ('id_venta', 'id_asesor', 'id_cliente', 'proyecto', 'unidad')
    list_filter = ('fecha_registro', 'fecha_promesa', 'fecha_escritura', 'concepto', 'proyecto')

class Parametros_ComisioneAdmin(admin.ModelAdmin):
    list_display = (
        'id_registro', 'periodo', 'id_asesor', 'meta_venta', 'venta_real',
        'renta_base', 'porcentaje_comision', 'porcentaje_bono_precio'
    )
    search_fields = ('id_asesor', 'periodo')
    list_filter = ('periodo',)

class Cierre_MesAdmin(admin.ModelAdmin):
    list_display = (
        'id_registro', 'fecha_inicio', 'fecha_fin')
    search_fields = ('fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio','fecha_fin')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(Banco, BancoAdmin)
admin.site.register(Uf, UfAdmin)
admin.site.register(ConjuntoParametros, ConjuntoParametrosAdmin)
admin.site.register(Comisione, ComisioneAdmin)
admin.site.register(Cierre_Mes, Cierre_MesAdmin)
admin.site.register(Parametros_Comisione, Parametros_ComisioneAdmin)
