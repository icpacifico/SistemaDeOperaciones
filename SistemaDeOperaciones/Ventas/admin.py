from django.contrib import admin
from .models import *
# Register your models here.

class VentasAdmin(admin.ModelAdmin):

    # fieldsets = (
        
        # ('Datos de la Solicitud',
        #     {'fields':
        #         (
        #             ('id_vivienda', 'id_cliente'),
        #         ),
        #     'classes': 'collapse'}
        # ),
        # ('Asignaciones de la solicitud',
        #     {'fields':
        #         (
        #             ('bodega', 'preparador'),
        #               ('estado_solicitud', 'observacion', 'is_active_solicitud')
        #         ),
        #     'classes': 'collapse wide'}
        # ),
    # )
    fieldsets = (
        ('Información General', {
            'fields': (
                'id_cotizacion', 
                'id_banco',
                'forma_pago',
                'tipo_pago',
                'estado_ven',
                'fecha_ven',
                'fecha_promesa_ven',
                'monto_reserva_ven',
                'descuento_manual_ven',
                'descuento_precio_ven',
                'descuento_adicional_ven',
                'descuento_ven',
                'pie_abono_ven',
                'pie_cancelado_ven',
                'pie_cobrar_ven',
            ),
        'classes': 'collapse'}),
        ('Montos', {
            'fields': (
                'monto_estacionamiento_ven',
                'monto_bodega_ven',
                'monto_vivienda_ven',
                'monto_vivienda_ingreso_ven',
                'monto_ven',
            )
        }),
        ('Comisiones', {
            'fields': (
                'factor_categoria_ven',
                'porcentaje_comision_ven',
                'promesa_porcentaje_comision_reparto_ven',
                'promesa_monto_comision_ven',
                'escritura_porcentaje_comision_reparto_ven',
                'escritura_monto_comision_ven',
                'total_comision_ven',
            )
        }),
        ('Bonos', {
            'fields': (
                'bono_vivienda_ven',
                'porcentaje_bono_precio_ven',
                'promesa_bono_precio_ven',
                'escritura_bono_precio_ven',
                'total_bono_precio_ven',
            )
        }),
        ('Otros', {
            'fields': (
                'numero_compra_ven',
                'cotizacion_ven',
                'monto_credito_ven',
                'monto_credito_real_ven',
                'pie_real_ven',
                'valor_factor_ven',
                'escritura_monto_comision_operacion_ven',
                'fecha_escritura_ven',
            ),
        'classes': 'collapse'}),
        
    )



admin.site.register(Profesion)
admin.site.register(Cliente)
admin.site.register(Cotizacion)
admin.site.register(Venta, VentasAdmin)
admin.site.register(TipoDesistimiento) # Quizás sea necesario moverlo al panel de admin
admin.site.register(Desistimiento)

