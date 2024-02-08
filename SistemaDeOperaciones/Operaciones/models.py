from django.db import models
from SistemaDeOperaciones.choices import *
from Ventas.models import Venta
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
        return str("(" + self.num_etapa + ")") + " - " + self.nombre_etapa

    class Meta:
        db_table = "etapa"

class CampoEtapa(models.Model):
    id_campo_etapa = models.AutoField(primary_key=True)
    id_etapa =  models.ForeignKey(Etapa,verbose_name="Etapa", on_delete=models.CASCADE)
    tipo_campo_etapa =  models.CharField(verbose_name="Tipo Campo", max_length=6, choices=TIPO_CAMPO_ETAPA, default=texto)
    nombre_campo_etapa = models.CharField(verbose_name="Nombre Campo", max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_campo_etapa

    class Meta:
        db_table = "campo_etapa"


class Operacione(models.Model):
    id_operacion = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(Venta, verbose_name="Venta", on_delete=models.CASCADE)
    id_etapa =  models.ForeignKey(Etapa, verbose_name="Etapa", on_delete=models.CASCADE)
    fecha_operacion = models.DateField(auto_now=True, verbose_name="Fecha Registro")
    comentario = models.TextField(verbose_name="Comentario")

    def __str__(self):
        return self.id_operacion

    class Meta:
        db_table = "operaciones"
