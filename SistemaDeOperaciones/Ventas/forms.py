from django import forms
from .models import Cliente, Cotizacion, Venta, TipoDesistimiento, Desistimiento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_nacionalidad', 'region', 'genero', 'estado_civil', 'id_profesion',
            'estado_cliente', 'rut_cliente', 'pasaporte_cliente', 'nombre_cliente',
            'nombre2_cliente', 'apellido_paterno_cliente', 'apellido_materno_cliente',
            'fono_cliente', 'fono2_cliente', 'correo_cliente', 'correo2_cliente',
            'direccion_cliente', 'direccion_trabajo_cliente', 'fecha_nacimiento_cliente'
        ]
        labels = {
            'id_nacionalidad': 'Nacionalidad',
            'region': 'Región',
            'genero': 'Género',
            'estado_civil': 'Estado Civil',
            'id_profesion': 'Profesión',
            'estado_cliente': 'Estado',
            'rut_cliente': 'Rut cliente',
            'pasaporte_cliente': 'Pasaporte cliente',
            'nombre_cliente': '1er Nombre',
            'nombre2_cliente': '2do Nombre',
            'apellido_paterno_cliente': '1er Apellido',
            'apellido_materno_cliente': '2do Apellido',
            'fono_cliente': 'Fono 1',
            'fono2_cliente': 'Fono 2',
            'correo_cliente': 'Correo 1',
            'correo2_cliente': 'Correo 2',
            'direccion_cliente': 'Dirección',
            'direccion_trabajo_cliente': 'Dirección trabajo',
            'fecha_nacimiento_cliente': 'Fecha nacimiento',
        }
        widgets = {
            'id_nacionalidad': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Nacionalidad'}),
            'region': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Región'}),
            'genero': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Género'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado Civil'}),
            'id_profesion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Profesión'}),
            'estado_cliente': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado'}),
            'rut_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rut cliente'}),
            'pasaporte_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pasaporte cliente'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1er Nombre'}),
            'nombre2_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2do Nombre'}),
            'apellido_paterno_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1er Apellido'}),
            'apellido_materno_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2do Apellido'}),
            'fono_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fono 1'}),
            'fono2_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fono 2'}),
            'correo_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo 1'}),
            'correo2_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo 2'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'direccion_trabajo_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección trabajo'}),
            'fecha_nacimiento_cliente': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha nacimiento'}),
        }



class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = [
            'id_vivienda', 'id_cliente', 'fecha_cotizacion', 'fecha_promesa_cotizacion',
            'procentaje_credito_cotizacion', 'numero_cotizacion', 'canal_cotizacion',
            'preaprobacion_cotizacion', 'renta_cotizacion', 'estado_cotizacion'
        ]
        labels = {
            'id_vivienda': 'Vivienda',
            'id_cliente': 'Cliente',
            'fecha_cotizacion': 'Fecha Cotización',
            'fecha_promesa_cotizacion': 'Fecha Promesa',
            'procentaje_credito_cotizacion': 'Porcentaje Crédito',
            'numero_cotizacion': 'Número Cotización',
            'canal_cotizacion': 'Canal Cotización',
            'preaprobacion_cotizacion': 'Preaprobación Cotización',
            'renta_cotizacion': 'Renta Cotización',
            'estado_cotizacion': 'Estado Cotización'
        }
        widgets = {
            'id_vivienda': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Vivienda'}),
            'id_cliente': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Cliente'}),
            'fecha_cotizacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Cotización'}),
            'fecha_promesa_cotizacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Promesa'}),
            'procentaje_credito_cotizacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Porcentaje Crédito'}),
            'numero_cotizacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número Cotización'}),
            'canal_cotizacion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Canal Cotización'}),
            'preaprobacion_cotizacion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Preaprobación Cotización'}),
            'renta_cotizacion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Renta Cotización'}),
            'estado_cotizacion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado Cotización'}),
        }



class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'id_cotizacion', 'id_vivienda', 'id_vendedor', 'id_cliente', 'id_banco',
            'forma_pago', 'pie_abono_ven', 'tipo_pago', 'estado_ven', 'fecha_ven',
            'fecha_promesa_ven', 'monto_reserva_ven', 'descuento_manual_ven',
            'descuento_precio_ven', 'descuento_adicional_ven', 'descuento_ven',
            'pie_cancelado_ven', 'pie_cobrar_ven', 'monto_estacionamiento_ven',
            'monto_bodega_ven', 'monto_vivienda_ven', 'monto_vivienda_ingreso_ven',
            'monto_ven', 'factor_categoria_ven', 'porcentaje_comision_ven',
            'promesa_porcentaje_comision_reparto_ven', 'promesa_monto_comision_ven',
            'escritura_porcentaje_comision_reparto_ven', 'escritura_monto_comision_ven',
            'total_comision_ven', 'bono_vivienda_ven', 'porcentaje_bono_precio_ven',
            'promesa_bono_precio_ven', 'escritura_bono_precio_ven', 'total_bono_precio_ven',
            'numero_compra_ven', 'cotizacion_ven', 'monto_credito_ven', 'monto_credito_real_ven',
            'pie_real_ven', 'valor_factor_ven', 'escritura_monto_comision_operacion_ven',
            'fecha_escritura_ven'
        ]
        labels = {
            'id_cotizacion': 'Cotización',
            'id_vivienda': 'Vivienda',
            'id_vendedor': 'Vendedor',
            'id_cliente': 'Cliente',
            'id_banco': 'Banco',
            'forma_pago': 'Forma Pago',
            'pie_abono_ven': 'Pie Abono Venta',
            'tipo_pago': 'Tipo Pago',
            'estado_ven': 'Estado Venta',
            'fecha_ven': 'Fecha Venta',
            'fecha_promesa_ven': 'Fecha Promesa Venta',
            'monto_reserva_ven': 'Monto Reserva Venta',
            'descuento_manual_ven': 'Descuento Manual Venta',
            'descuento_precio_ven': 'Descuento Precio Venta',
            'descuento_adicional_ven': 'Descuento Adicional Venta',
            'descuento_ven': 'Descuento Venta',
            'pie_cancelado_ven': 'Pie Cancelado Venta',
            'pie_cobrar_ven': 'Pie Cobrar Venta',
            'monto_estacionamiento_ven': 'Monto Estacionamiento Venta',
            'monto_bodega_ven': 'Monto Bodega Venta',
            'monto_vivienda_ven': 'Monto Vivienda Venta',
            'monto_vivienda_ingreso_ven': 'Monto Vivienda Ingreso Venta',
            'monto_ven': 'Monto Venta',
            'factor_categoria_ven': 'Factor Categoria Venta',
            'porcentaje_comision_ven': 'Porcentaje Comision Venta',
            'promesa_porcentaje_comision_reparto_ven': 'Promesa Porcentaje Comision Reparto Venta',
            'promesa_monto_comision_ven': 'Promesa Monto Comision Venta',
            'escritura_porcentaje_comision_reparto_ven': 'Escritura Porcentaje Comision Reparto Venta',
            'escritura_monto_comision_ven': 'Escritura Monto Comision Venta',
            'total_comision_ven': 'Total Comision Venta',
            'bono_vivienda_ven': 'Bono Vivienda Venta',
            'porcentaje_bono_precio_ven': 'Porcentaje Bono Precio Venta',
            'promesa_bono_precio_ven': 'Promesa Bono Precio Venta',
            'escritura_bono_precio_ven': 'Escritura Bono Precio Venta',
            'total_bono_precio_ven': 'Total Bono Precio Venta',
            'numero_compra_ven': 'Numero Compra Venta',
            'cotizacion_ven': 'Cotización Venta',
            'monto_credito_ven': 'Monto Crédito Venta',
            'monto_credito_real_ven': 'Monto Crédito Real Venta',
            'pie_real_ven': 'Pie Real Venta',
            'valor_factor_ven': 'Valor Factor Venta',
            'escritura_monto_comision_operacion_ven': 'Escritura Monto Comisión Operación Venta',
            'fecha_escritura_ven': 'Fecha Escritura Venta'
        }
        widgets = {
            'id_cotizacion': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Cotización'}),
            'id_vivienda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vivienda'}),
            'id_vendedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendedor'}),
            'id_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cliente'}),
            'id_banco': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Banco'}),
            'forma_pago': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Forma Pago'}),
            'pie_abono_ven': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Pie Abono Venta'}),
            'tipo_pago': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Tipo Pago'}),
            'estado_ven': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Estado Venta'}),
            'fecha_ven': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Venta'}),
            'fecha_promesa_ven': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Promesa Venta'}),
            'monto_reserva_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Reserva Venta'}),
            'descuento_manual_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento Manual Venta'}),
            'descuento_precio_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento Precio Venta'}),
            'descuento_adicional_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento Adicional Venta'}),
            'descuento_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento Venta'}),
            'pie_cancelado_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pie Cancelado Venta'}),
            'pie_cobrar_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pie Cobrar Venta'}),
            'monto_estacionamiento_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Estacionamiento Venta'}),
            'monto_bodega_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Bodega Venta'}),
            'monto_vivienda_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Vivienda Venta'}),
            'monto_vivienda_ingreso_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Vivienda Ingreso Venta'}),
            'monto_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Venta'}),
            'factor_categoria_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Factor Categoria Venta'}),
            'porcentaje_comision_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Porcentaje Comision Venta'}),
            'promesa_porcentaje_comision_reparto_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promesa Porcentaje Comision Reparto Venta'}),
            'promesa_monto_comision_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promesa Monto Comision Venta'}),
            'escritura_porcentaje_comision_reparto_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escritura Porcentaje Comision Reparto Venta'}),
            'escritura_monto_comision_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escritura Monto Comision Venta'}),
            'total_comision_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Comision Venta'}),
            'bono_vivienda_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bono Vivienda Venta'}),
            'porcentaje_bono_precio_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Porcentaje Bono Precio Venta'}),
            'promesa_bono_precio_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Promesa Bono Precio Venta'}),
            'escritura_bono_precio_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escritura Bono Precio Venta'}),
            'total_bono_precio_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Bono Precio Venta'}),
            'numero_compra_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero Compra Venta'}),
            'cotizacion_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cotización Venta'}),
            'monto_credito_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Crédito Venta'}),
            'monto_credito_real_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto Crédito Real Venta'}),
            'pie_real_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pie Real Venta'}),
            'valor_factor_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor Factor Venta'}),
            'escritura_monto_comision_operacion_ven': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escritura Monto Comisión Operación Venta'}),
            'fecha_escritura_ven': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Escritura Venta'}),
        }



class TipoDesistimientoForm(forms.ModelForm):
    class Meta:
        model = TipoDesistimiento
        fields = ['nombre_tipodesistimiento']
        labels = {'nombre_tipodesistimiento': 'Nombre del Tipo de Desistimiento'}
        widgets = {'nombre_tipodesistimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Tipo de Desistimiento'})}

class DesistimientoForm(forms.ModelForm):
    class Meta:
        model = Desistimiento
        fields = ['id_venta', 'comentario_desistimiento', 'id_tipodesistimiento']
        labels = {
            'id_venta': 'Venta',
            'comentario_desistimiento': 'Comentario',
            'id_tipodesistimiento': 'Tipo de Desistimiento',
        }
        widgets = {
            'id_venta': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venta'}),
            'comentario_desistimiento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comentario'}),
            'id_tipodesistimiento': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Tipo de Desistimiento'}),
        }
