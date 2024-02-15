from django.db import models
from SistemaDeOperaciones.choices import *
from Ventas.models import *
from Proyectos.models import Vivienda
from Administracion.models import Banco, Nacionalidad
from SistemaDeOperaciones.choices import *
# Create your models here.

class CategoriaEtapa(models.Model):
    id_categoria_etapa = models.AutoField(primary_key=True)
    nombre_categoria_etapa = models.CharField(verbose_name="Nombre Categoria", max_length=50, blank=True, null=True)
    orden_categoria_etapa = models.IntegerField(verbose_name="Orden Categoria", blank=True, null=True)

    def __str__(self):
        return self.nombre_categoria_etapa

    class Meta:
        db_table = "categoria_etapa"


class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    id_categoria_etapa = models.ForeignKey(CategoriaEtapa,verbose_name="Categoria", on_delete=models.CASCADE)
    forma_pago =  models.CharField(verbose_name="Categoria", max_length=30, choices=FORMA_PAGO_CHOICES, default=credito)
    estado_etapa =  models.CharField(verbose_name="Estado", max_length=15, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_etapa = models.CharField(verbose_name="Nombre Etapa", max_length=50, blank=True, null=True)
    alias_etapa = models.CharField(verbose_name="Alias Etapa", max_length=50, blank=True, null=True)
    num_etapa = models.IntegerField(verbose_name="N° Etapa", blank=True, null=True)
    duracion_etapa = models.FloatField(verbose_name="Duración Etapa", blank=True, null=True)
    num_real_etapa = models.IntegerField(verbose_name="N° real Etapa", blank=True, null=True)

    def __str__(self):
        return "(" + str(self.num_etapa) + ")" + " - " + self.nombre_etapa

    class Meta:
        db_table = "etapa"


class VentaOp(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    # id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco, on_delete=models.CASCADE) # PENDIENTE
    forma_pago = models.CharField(verbose_name="Forma Pago", max_length=30, choices=FORMA_PAGO_CHOICES, default=credito)
    estado_ven = models.CharField(verbose_name="Estado Venta", max_length=20, choices=EST_VENTA_CHOICES, default=activa)
    fecha_ven = models.DateTimeField(verbose_name="Fecha Venta", null=True, blank=True)
    monto_ven = models.FloatField(verbose_name="Monto Venta", null=True, blank=True)


    def __str__(self):
        return "(" +str(self.id_venta)+")"+" - "+str(self.id_vivienda)+" - "+str(self.id_cliente)

    class Meta:
        db_table = "ventaop"
class Operacione(models.Model):
    id_operacion = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(VentaOp, verbose_name="Venta", on_delete=models.CASCADE)
    id_etapa =  models.ForeignKey(Etapa, verbose_name="Etapa", on_delete=models.CASCADE)
    fecha_operacion = models.DateField(verbose_name="Fecha Registro")
    comentario = models.TextField(verbose_name="Comentario")

    def __str__(self):
        return str(self.id_operacion)

    class Meta:
        db_table = "operaciones"
