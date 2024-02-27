from django.db import models
from Proyectos.models import Vivienda
from Administracion.models import *
from SistemaDeOperaciones.choices import *


# Create your models here.



class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=9, verbose_name="Rut")
    id_nacionalidad = models.ForeignKey(Nacionalidad, verbose_name="Nacionalidad",
                                        on_delete=models.CASCADE)  # PENDIENTE
    region = models.CharField(verbose_name="Región", max_length=31, choices=REGIONES_CHOICES, default=iv_reg_coquimbo)
    genero = models.CharField(verbose_name="Género", max_length=30, choices=SEXO_CHOICES, default=sin_definir)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=30, choices=ESTADO_CIVIL_CHOICES,
                                    default=casado_a)
    id_profesion = models.ForeignKey(Profesion, verbose_name="Profesión", on_delete=models.CASCADE)  # PENDIENTE
    estado_cliente = models.CharField(verbose_name="Estado", max_length=50, choices=IS_ACTIVE_CHOICES,
                                          default=is_active)
    rut_cliente = models.CharField(verbose_name="Rut cliente", max_length=18, null=True, blank=True)
    pasaporte_cliente = models.CharField(verbose_name="Pasaporte cliente", max_length=50, null=True, blank=True)
    nombre_cliente = models.CharField(verbose_name="1er Nombre", max_length=150, null=True, blank=True)
    nombre2_cliente = models.CharField(verbose_name="2do Nombre", max_length=150, null=True, blank=True)
    apellido_paterno_cliente = models.CharField(verbose_name="1er Apellido", max_length=150, null=True, blank=True)
    apellido_materno_cliente = models.CharField(verbose_name="2do Apellido", max_length=150, null=True, blank=True)
    fono_cliente = models.CharField(verbose_name="Fono 1", max_length=15, null=True, blank=True)
    fono2_cliente = models.CharField(verbose_name="Fono 2", max_length=15, null=True, blank=True)
    correo_cliente = models.CharField(verbose_name="Correo 1", max_length=150, null=True, blank=True)
    correo2_cliente = models.CharField(verbose_name="Correo 2", max_length=150, null=True, blank=True)
    direccion_cliente = models.CharField(verbose_name="Dirección ", max_length=150, null=True, blank=True)
    direccion_trabajo_cliente = models.CharField(verbose_name="Dirección trabajo", max_length=150, null=True, blank=True)
    fecha_nacimiento_cliente = models.DateField(verbose_name="Fecha nacimiento", null=True, blank=True)

    def __str__(self):
        return "("+str(self.rut_cliente)+")"+" - "+self.nombre_cliente +" "+self.apellido_paterno_cliente+" "+self.apellido_materno_cliente

    class Meta:
        db_table = "cliente"


class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField(verbose_name="Fecha Cotización", null=True, blank=True ) 
    fecha_promesa_cotizacion = models.DateField(verbose_name="Fecha Promesa", null=True, blank=True ) 
    procentaje_credito_cotizacion = models.FloatField(verbose_name="Porcentaje Credito", null=True, blank=True)
    numero_cotizacion = models.IntegerField(verbose_name="Estado Venta",  null=True, blank=True)
    canal_cotizacion = models.CharField(verbose_name="Canal Cotización", max_length=200, choices=CANAL_COTIZACION_CHOICES, default=None)
    preaprobacion_cotizacion = models.CharField(verbose_name="Preaprobación Cotización", max_length=200, choices=PREAPROBACION_COTIZACION_CHOICES, default=None)
    renta_cotizacion = models.CharField(verbose_name="Renta Cotización", max_length=200, choices=RENTA_COTIZACION_CHOICES, default=None)
    estado_cotizacion = models.CharField(verbose_name="Renta Cotización", max_length=200, choices=IS_ACTIVE_CHOICES, default=None)

   # def __str__(self):
    #    return "(" +str(self.id_cotizacion)+")Hola"
    class Meta:
        db_table = "cotizacion"

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_vivienda = models.CharField(verbose_name="Vivienda", max_length=2,) # ForeignKey(Vivienda, on_delete=models.CASCADE) #TODO: Esta en cotizacion ver si es posible visualizar desde FK
    id_vendedor = models.CharField(verbose_name="Vendedor", max_length=2,) # ForeignKey(Vendedor, on_delete=models.CASCADE) #TODO: Esta en cotizacion ver si es posible visualizar desde FK
    id_cliente = models.CharField(verbose_name="Cliente", max_length=2,) # ForeignKey(Cliente, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE) # PENDIENTE
    # id_pie_ven = models.ForeignKey(PieVenta, on_delete=models.CASCADE)
    forma_pago = models.CharField(verbose_name="Forma Pago", max_length=30, choices=FORMA_PAGO_CHOICES, default=credito)
    # id_descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE) # PENDIENTE
    # id_premio = models.ForeignKey(Premio, on_delete=models.CASCADE) # PENDIENTE
    pie_abono_ven = models.CharField(verbose_name="Pie Abono Venta", max_length=2, choices=SI_NO_CHOICES, default=None)
    tipo_pago = models.CharField(verbose_name="Tipo Pago", max_length=20, choices=TIPO_PAGO, default=None)
    estado_ven = models.CharField(verbose_name="Estado Venta", max_length=20, choices=EST_VENTA_CHOICES, default=activa)
    fecha_ven = models.DateTimeField(verbose_name="Fecha Venta", null=True, blank=True)
    fecha_promesa_ven = models.DateTimeField(verbose_name="Fecha Promsa Venta", null=True, blank=True)
    monto_reserva_ven = models.FloatField(verbose_name="Monto Reserva Venta", null=True, blank=True)
    descuento_manual_ven = models.FloatField(verbose_name="Desciento Manual Venta", null=True, blank=True)
    descuento_precio_ven = models.FloatField(verbose_name="Descuento Precio Venta", null=True, blank=True)
    descuento_adicional_ven = models.FloatField(verbose_name="Descuento Adicional Venta", null=True, blank=True)
    descuento_ven = models.FloatField(verbose_name="Descuento Venta", null=True, blank=True)
    pie_cancelado_ven = models.FloatField(verbose_name="Pie Cancelado Venta", null=True, blank=True)
    pie_cobrar_ven = models.FloatField(verbose_name="Pie Cobrar Venta", null=True, blank=True)
    monto_estacionamiento_ven = models.FloatField(verbose_name="Monto Estacionamiento Venta", null=True, blank=True)
    monto_bodega_ven = models.FloatField(verbose_name="Monto Bodega Venta", null=True, blank=True)
    monto_vivienda_ven = models.FloatField(verbose_name="Monto Vivienda Venta", null=True, blank=True)
    monto_vivienda_ingreso_ven = models.FloatField(verbose_name="Monto Vivienda Ingreso Venta", null=True, blank=True)
    monto_ven = models.FloatField(verbose_name="Monto Venta", null=True, blank=True)
    factor_categoria_ven = models.FloatField(verbose_name="Factor Categoria Venta", null=True, blank=True)
    porcentaje_comision_ven = models.FloatField(verbose_name="Porcentaje Comision Venta", null=True, blank=True)
    promesa_porcentaje_comision_reparto_ven = models.FloatField(
        verbose_name="Promesa Porcentaje Comision Reparto Venta", null=True, blank=True)
    promesa_monto_comision_ven = models.FloatField(verbose_name="Promesa Monto Comision Venta", null=True, blank=True)
    # promesa_monto_comision_supervisor_ven = models.FloatField(verbose_name = "Promesa Monto Comision Supervisor Venta",null=True, blank=True)
    # promesa_monto_comision_jefe_ven = models.FloatField(verbose_name = "Promesa Monto Comision Jefe Venta",null=True, blank=True)
    escritura_porcentaje_comision_reparto_ven = models.FloatField(
        verbose_name="Escritura Porcetaje Comision Reparto Venta", null=True, blank=True)
    escritura_monto_comision_ven = models.FloatField(verbose_name="Escritura Monto Comision Venta", null=True,
                                                     blank=True)
    # escritura_monto_comision_supervisor_ven = models.FloatField(verbose_name = "Escritura Monto Comision Supervisor Venta",null=True, blank=True)
    # escritura_monto_comision_jefe_ven = models.FloatField(verbose_name = "Escritura Monto Comision Jefe Venta",null=True, blank=True)
    total_comision_ven = models.FloatField(verbose_name="Total Comision Venta", null=True, blank=True)
    # total_comision_supervisor_ven = models.FloatField(verbose_name = "Total Comision Supervisor Venta",null=True, blank=True)
    # total_comision_jefe_ven = models.FloatField(verbose_name = "Total Comision Jefe Venta",null=True, blank=True)
    bono_vivienda_ven = models.FloatField(verbose_name="Bono Vivienda Venta", null=True, blank=True)
    porcentaje_bono_precio_ven = models.FloatField(verbose_name="Porcentaje Bono Precio Venta", null=True, blank=True)
    promesa_bono_precio_ven = models.FloatField(verbose_name="Promesa Bono Precio Venta", null=True, blank=True)
    # promesa_bono_precio_supervisor_ven = models.FloatField(verbose_name = "Promesa Bono Precio Supervisor Venta",null=True, blank=True)
    # promesa_bono_precio_jefe_ven = models.FloatField(verbose_name = "Promesa Bono Precio Jefe Venta",null=True, blank=True)
    escritura_bono_precio_ven = models.FloatField(verbose_name="Escritura Bono Precio Jefe Venta", null=True,
                                                  blank=True)
    # escritura_bono_precio_supervisor_ven = models.FloatField(verbose_name = "Escritura Bono Precio Supervisor Venta",null=True, blank=True)
    # escritura_bono_precio_jefe_ven = models.FloatField(verbose_name = "Escritura Bono Precio Jefe Venta",null=True, blank=True)
    total_bono_precio_ven = models.FloatField(verbose_name="Total Bono Precio Venta", null=True, blank=True)
    # total_bono_precio_supervisor_ven = models.FloatField(verbose_name = "Total Bono Precio Supervisor Venta",null=True, blank=True)
    # total_bono_precio_jefe_ven = models.FloatField(verbose_name = "Total Bono Precio Jefe Venta",null=True, blank=True)
    numero_compra_ven = models.IntegerField(verbose_name="Numero Compra Venta", null=True, blank=True)
    cotizacion_ven = models.IntegerField(verbose_name="Cotizacion Venta", null=True, blank=True)
    monto_credito_ven = models.FloatField(verbose_name="Monto Credito Venta", null=True, blank=True)
    monto_credito_real_ven = models.FloatField(verbose_name="Monto Credito Real Venta", null=True, blank=True)
    pie_real_ven = models.FloatField(verbose_name="Pie Real Venta", null=True, blank=True)
    valor_factor_ven = models.FloatField(verbose_name="Valor Factor Venta", null=True, blank=True)
    # id_supervisor_ven = models.IntegerField(null=True, blank=True)
    # id_jefe_ven = models.IntegerField(null=True, blank=True)
    # id_operacion_ven = models.IntegerField(null=True, blank=True)
    escritura_monto_comision_operacion_ven = models.FloatField(verbose_name="Escritura Monto Comision Operaicion Venta",
                                                               null=True, blank=True)
    fecha_escritura_ven = models.DateField(verbose_name="Fecha", null=True, blank=True)

    def __str__(self):
        return "(" +str(self.id_venta)+")"

    class Meta:
        db_table = "venta"

class TipoDesistimiento(models.Model):
    id_tipodesistimiento = models.AutoField(primary_key=True)
    nombre_tipodesistimiento = models.CharField(max_length=50)

    def __str__(self):
        return "(" +str(self.id_tipodesistimiento)+")"+"-"+self.nombre_tipodesistimiento

    class Meta:
        db_table = "tipodesistimiento"

class Desistimiento(models.Model):
    id_desistimiento = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, verbose_name="Venta", on_delete=models.CASCADE)
    comentario_desistimiento = models.CharField(max_length=50, verbose_name="Comentario")
    id_tipodesistimiento = models.ForeignKey(TipoDesistimiento, verbose_name="Tipo", on_delete=models.CASCADE)

    def __str__(self):
        return "(" +str(self.id_desistimiento)+")"+"-"+self.id_tipodesistimiento.nombre_tipodesistimiento

    class Meta:
        db_table = "desistimiento"

