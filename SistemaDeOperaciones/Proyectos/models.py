from django.db import models
from SistemaDeOperaciones.choices import *

# Create your models here.

class Condominio(models.Model):
    id_condominio = models.AutoField(primary_key=True)
    estado_condominio = models.CharField(verbose_name="Estado",max_length=30, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_condominio = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    fecha_venta_condominio = models.DateField(verbose_name="Fecha Venta Condominio", null=True, blank=True)

    def __str__(self):
        return str("(" + self.id_condominio + ")") + " - " + self.nombre_condominio

    class Meta:
        db_table = "condominio"

class Etapa(models.Model):
    id_etapa = models.AutoField()
    nombre_etapa = models.CharField(max_length=50)
    id_condominio = models.ForeignKey(Condominio, verbose_name="Condominio", on_delete=models.CASCADE)

    def __str__(self):
        return str("(" + self.id_condominio + ")") + " - " + self.nombre_etapa

    class Meta:
        db_table = "etapa"
class Torre(models.Model):
    id_torre = models.AutoField(primary_key=True)
    id_etapa = models.ForeignKey(Etapa, verbose_name="Etapa", on_delete=models.CASCADE)
    estado_torre = models.CharField(verbose_name="Estado",max_length=30, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_torre = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)

    def __str__(self):
        return str("(" + self.id_torre + ")") + " - " + self.nombre_torre

    class Meta:
        db_table = "torre"

class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    estado_modelo = models.CharField(verbose_name="Estado",max_length=30, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_modelo = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    numero_cama_modelo = models.IntegerField(verbose_name="N° camas", null=True, blank=True)
    numero_bagno_modelo = models.IntegerField(verbose_name="N° baños", null=True, blank=True)
    descripcion_modelo = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return str("(" + self.id_modelo + ")") + " - " + self.nombre_modelo

    class Meta:
        db_table = "modelo"

class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    id_etapa = models.ForeignKey(Etapa, verbose_name="Etapa", on_delete=models.CASCADE)
    estado_bodega = models.CharField(verbose_name="Estado",max_length=30, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_bodega = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    valor_bodega = models.FloatField(verbose_name="Valor", null=True, blank=True)
    rol_bodega = models.CharField(verbose_name="Rol", max_length=100, null=True, blank=True)

    def __str__(self):
        return str("(" + self.id_bodega + ")") + " - " + self.nombre_bodega

    class Meta:
        db_table = "bodega"

class Estacionamiento(models.Model):
    id_estacionamiento = models.AutoField(primary_key=True)
    id_etapa = models.ForeignKey(Etapa, verbose_name="Etapa", on_delete=models.CASCADE)
    estado_estacionamiento = models.CharField(verbose_name="Estado",max_length=30, choices=IS_DISPONIBLE_CHOICES, default=disponible)
    nombre_estacionamiento = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    valor_estacionamiento = models.FloatField(verbose_name="Valor", null=True, blank=True)

    def __str__(self):
        return str("(" + self.id_estacionamiento + ")") + " - " + self.nombre_estacionamiento

    class Meta:
        db_table = "estacionamiento"

class Vivienda(models.Model):

    id_vivienda = models.AutoField(primary_key=True)
    id_torre = models.ForeignKey(Torre, verbose_name="Torre", on_delete=models.CASCADE)
    id_modelo = models.ForeignKey(Modelo, verbose_name="Modelo", on_delete=models.CASCADE)
    tipo_vivienda = models.CharField(verbose_name="Tipo", max_length=30, choices=TIPO_VIVIENDA, default=departamento)
    ori_vivienda = models.CharField(verbose_name="Orientación", max_length=30, choices=ORIENTACION_VIVIENDA,
                                    default=norte)
    estado_vivienda = models.CharField(verbose_name="Estado vivienda", max_length=30, choices=IS_DISPONIBLE_CHOICES,
                                       default=disponible)
    piso = models.CharField(verbose_name="Piso", max_length=30, choices=PISO, default=uno)
    nombre_vivienda = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    valor_vivienda = models.FloatField(verbose_name="Valor", null=True, blank=True)
    metros_vivienda = models.FloatField(verbose_name="Metros depto", null=True, blank=True)
    metros_terraza_vivienda = models.FloatField(verbose_name="Metros terraza", null=True, blank=True)
    metros_total_vivienda = models.FloatField(verbose_name="Metros total", null=True, blank=True)
    bono_vivienda = models.FloatField(verbose_name="Bono", null=True, blank=True)
    prorrateo_vivienda = models.FloatField(verbose_name="Prorrateo", null=True, blank=True)
    rol_vivienda = models.CharField(verbose_name="Rol", max_length=100, null=True, blank=True)

    def __str__(self):
        return str("(id: " + self.id_vivienda + ")") + " - Depto: " + self.nombre_vivienda

    class Meta:
        db_table = "vivienda"