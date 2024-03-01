from django.db import models
from Ventas.models import Venta
from Administracion.models import Banco
from SistemaDeOperaciones.choices import *

# Create your models here.


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    forma_pago = models.CharField(verbose_name="Forma Pago", max_length=30, choices=FORMA_PAGO_CHOICES, default=contado)
    id_venta =  models.ForeignKey(Venta,verbose_name="Venta", on_delete=models.CASCADE)
    id_banco = models.ForeignKey(Banco,verbose_name="Banco", on_delete=models.CASCADE)
    categoria_pago = models.CharField(verbose_name="Categoria Pago", max_length=30, choices=CATEGORIA_PAGO_CHOICES, default=cierre_negocio)
    estado_pago =  models.CharField(verbose_name="Estado Pago", max_length=30, choices=EST_PAGO_CHOICES, default=pendiente)
    numero_documento = models.CharField(verbose_name="N° Documento",max_length=10)
    numero_serie = models.CharField(verbose_name="N° Serie",max_length=10)
    fecha_pago =  models.DateField(verbose_name="Fecha Pago",)
    fecha_real_pago = models.DateField(verbose_name="Fecha Real pago",)
    monto_pago = models.IntegerField(verbose_name="Monto Pago",)
    descripcion = models.CharField(verbose_name="Descripción",max_length=100)

    def __str__(self):
        return self.id_pago

    class Meta:
        db_table = "pagos"
