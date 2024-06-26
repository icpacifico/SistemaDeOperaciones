from django.db import models
from Proyectos.models import Condominio
from SistemaDeOperaciones.funciones import validate_positive_integer
from django.contrib.auth.models import User
from SistemaDeOperaciones.choices import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='foto_perfil')

    def __str__(self):
        return f'{self.user.username} Profile'  # show how we want it to be displayed


# Create your models here.
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    nombre_nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50, null=False, blank=False)

    def __str__(self):
        return "(" + str(self.id_nacionalidad) + ")" + " " + self.nombre_nacionalidad

    class Meta:
        db_table = "nacionalidad"


class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(unique=True, verbose_name="Banco", max_length=50, null=False, blank=False)

    def __str__(self):
        return "(" + str(self.id_banco) + ")" + " " + self.nombre_banco

    class Meta:
        db_table = "banco"


class Uf(models.Model):
    id_registro = models.AutoField(primary_key=True)
    valor_uf = models.FloatField(verbose_name="UF", null=False, blank=False)
    fecha_registro = models.DateField(verbose_name="Fecha de UF")

    def __str__(self):
        return "(" + str(self.fecha_registro) + ")" + " " + str(self.valor_uf)

    class Meta:
        db_table = "valores_uf"


class ConjuntoParametros(models.Model):
    id_conjunto_parametros = models.AutoField(primary_key=True)
    id_condominio = models.ForeignKey(Condominio, verbose_name="Condominio", on_delete=models.CASCADE)
    factor_vendedor = models.IntegerField(verbose_name="Factor", validators=[validate_positive_integer], null=False,
                                          blank=False)
    precio_dcto_depto = models.FloatField(verbose_name="Precio descuento Depto", validators=[validate_positive_integer],
                                          null=False, blank=False)
    bono_precio_porce = models.IntegerField(verbose_name="Porcentaje Bono Precio",
                                            validators=[validate_positive_integer], null=False, blank=False)
    porcen_promesa = models.FloatField(verbose_name="Porcentaje Promesa", validators=[validate_positive_integer],
                                       null=False, blank=False)
    porcen_escritura = models.FloatField(verbose_name="Porcentaje Escritura", validators=[validate_positive_integer],
                                         null=False, blank=False)
    porcen_comision_vendedor = models.FloatField(verbose_name="% comisión Vendedor",
                                                 validators=[validate_positive_integer], null=False, blank=False)
    monto_escrt_operaciones = models.IntegerField(verbose_name="Monto Escritura Operaciones (UF)",
                                                  validators=[validate_positive_integer], null=False, blank=False)
    monto_reserva = models.IntegerField(verbose_name="Monto Reserva (UF)", validators=[validate_positive_integer],
                                        null=False, blank=False)
    monto_prorrateo = models.IntegerField(verbose_name="Monto a Prorratear", validators=[validate_positive_integer],
                                          null=False, blank=False)
    monto_recuperar = models.IntegerField(verbose_name="Monto a  Recuperar", validators=[validate_positive_integer],
                                          null=False, blank=False)
    fecha_recuperacion = models.DateField(verbose_name="Fecha Recuperación", null=False, blank=False)
    valor_bodega = models.IntegerField(verbose_name="$ Bodega", validators=[validate_positive_integer], null=False,
                                       blank=False)
    valor_estacionamiento = models.IntegerField(verbose_name="$ Estacionamiento",
                                                validators=[validate_positive_integer], null=False, blank=False)
    fecha_termino_venta = models.DateField(verbose_name="Fecha termino de ventas", null=False, blank=False)
    direccion_condominio = models.CharField(max_length=100, verbose_name="Dirección Condominio", null=False,
                                            blank=False)
    banco_alzante = models.ForeignKey(Banco, verbose_name="Banco Alzante", on_delete=models.CASCADE, null=False,
                                      blank=False)

    def __str__(self):
        return "(" + str(self.id_conjunto_parametros) + ")" + " " + self.id_condominio.nombre_condominio

    class Meta:
        db_table = "parametros"


class Profesion(models.Model):
    id_profesion = models.AutoField(primary_key=True)
    nombre_profesion = models.CharField(verbose_name="Profesion", max_length=50, null=False, blank=False)

    def __str__(self):
        return "(" + str(self.id_profesion) + ")" + " - " + self.nombre_profesion

    class Meta:
        db_table = "profesion"


class ConsolidadoComisione(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    proyecto = models.CharField(verbose_name="Proyecto asociado",
                                max_length=10)  # Poryecto al cual se asocia la comisión
    etapa = models.CharField(verbose_name="Etapa asociada", max_length=10)  # Etapa asociada a la comisión+
    unidad = models.CharField(verbose_name="Unidad vendida", max_length=10)  # Unidad asociada a la comisión
    venta_origen = models.IntegerField()
    asesor_origen = models.IntegerField()
    tipo_registro = models.CharField(max_length=40)
    monto_comisionar = models.IntegerField()
    estado_comision = models.CharField(max_length=50)
    estado_registro = models.CharField(max_length=50)

    class Meta:
        db_table = "consolidado_comisiones"


class Cierre_Mes(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return "ID:" + str(self.id_registro) + " - Desde:" + str(self.fecha_inicio)  + " hasta " + str(self.fecha_fin)

    class Meta:
        db_table = "cierre_mes"


"""
class CierreComisione(models.Model):
    id_registro = models.AutoField(primary_key=True)
    fecha_registro = models.DateField()
    id_registro_cm = models.IntegerField()
    id_registro_cc = models.IntegerField()
    concepto = models.CharField(max_length=50)
    valor_uf = models.FloatField()
    porcentaje_comision = models.FloatField()
    monto_comisionar = models.FloatField()
    monto_comision_uf = models.FloatField()
    monto_comision_clp = models.FloatField()
    bono_precio_uf = models.FloatField(verbose_name="Monto Bono Precio en UF",
                                       blank=True)  # Corresponde al monto en UF a pagar por concepto de Bono precio
    bono_precio_promesa_uf = models.FloatField(verbose_name="Monto Bono Precio Promesa en UF",
                                               blank=True)  # Corresponde al 60% del Bono precio que se pagará por paso a promesa
    bono_precio_promesa_clp = models.FloatField(verbose_name="Monto Bono Precio Promesa en CLP",
                                                blank=True)  # Corresponde al 60% del Bono precio que se pagará por paso a promesa
    bono_precio_escritura_uf = models.FloatField(verbose_name="Monto Bono Precio esctitura en UF",
                                                 blank=True)  # Corresponde al 40% del Bono precio que se pagará por paso a escritura
    bono_precio_escritura_clp = models.FloatField(verbose_name="Monto Bono Precio Escritura en CLP",
                                                  blank=True)  # Corresponde al 40% del Bono precio que se pagará por paso a escritura
    monto_bono_c1 = models.FloatField(verbose_name="Monto Bono C1", blank=True)  # Corresponde al bono C1 de icp
    monto_bono_c2 = models.FloatField(verbose_name="Monto Bono C2", blank=True)  # Corresponde al bono C2 de icp
    monto_bono_c3 = models.FloatField(verbose_name="Monto Bono C3", blank=True)  # Corresponde al bono C3 de icp
    monto_desistimiento = models.FloatField(verbose_name="Monto Desistimiento", blank=True)
    total_comisiones = models.FloatField(verbose_name="Total Comisiones")
    saldo_pagar = models.FloatField(verbose_name="Saldo a pagar del Total Comisiones")
    total_bonos = models.FloatField(verbose_name="Total Bonos")
    total_bonos_comisiones = models.FloatField(verbose_name="Total Bonos + Comisiones")

    class Meta:
        db_table = "cierre_comisiones"
        
"""

class Comisione(models.Model):
    id_comision = models.AutoField(primary_key=True)
    id_venta = models.CharField(verbose_name="Id Venta", max_length=10)  # Refeencia a la venta
    id_asesor = models.CharField(verbose_name="Id Asesor", max_length=10)  # Referencia al asesor
    id_cliente = models.CharField(verbose_name="Id Cliente",
                                  max_length=10)  # CLiente asociado a la undad que paga comision
    fecha_registro = models.DateField(verbose_name="Fecha Registro")
    fecha_promesa = models.DateField(verbose_name="Fecha Promesa", blank=True)
    fecha_escritura = models.DateField(verbose_name="Fecha Escritura", blank=True)
    fecha_desistimiento = models.DateField(verbose_name="Fecha Desistimiento", blank=True)
    valor_uf = models.FloatField(verbose_name="Valor UF", blank=True)  # Corresponde a la UF de la fecha en que se pacta la comisión
    concepto = models.CharField(verbose_name="Concepto del Registro",
                                max_length=10, blank=True)  # Concepto por el cual se registra la comision
    proyecto = models.CharField(verbose_name="Proyecto asociado",
                                max_length=10, blank=True)  # Poryecto al cual se asocia la comisión
    etapa = models.CharField(verbose_name="Etapa asociada", max_length=10, blank=True)  # Etapa asociada a la comisión+
    unidad = models.CharField(verbose_name="Unidad vendida", max_length=10, blank=True)  # Unidad asociada a la comisión
    bono_precio = models.CharField(verbose_name="Aplica Bono Precio", choices=SI_NO_CHOICES, default="No",
                                   max_length=2, blank=True)  # Indica si la omisión llevrá bono precio
    monto_venta = models.FloatField(verbose_name="Monto Final Venta",
                                    max_length=10, blank=True)  # Indica el monto de la venta sobre la que será calcula la comisión del asesor
    porcentaje_comision = models.FloatField(
        verbose_name="Porcentaje Comisión", blank=True)  # Equivalente al porcentaje de comisión según el cumplimiento de la ventas
    comision_uf = models.FloatField(
        verbose_name="Monto Comisión UF", blank=True)  # Corresponde al monto total a pagar por la comisión
    comision_promesa_uf = models.FloatField(
        verbose_name="Monto Comisión x promesa en UF", blank=True)  # Corresponde al 60% de la comisión que se pagará por paso a promesa
    comision_promesa_clp = models.FloatField(
        verbose_name="Monto Comisión x promesa en CLP", blank=True)  # Corresponde al 60% de la comisión que se pagará por paso a promesa
    comision_escritura_uf = models.FloatField(verbose_name="Monto Comisión x escritura en UF",
                                              blank=True)  # Corresponde al 40% de la comisión que se pagará por paso a escritura
    comision_escritura_clp = models.FloatField(verbose_name="Monto Comisión x escritura en CLP",
                                               blank=True)  # Corresponde al 40% de la comisión que se pagará por paso a escritura
    bono_precio_uf = models.FloatField(verbose_name="Monto Bono Precio en UF",
                                       blank=True)  # Corresponde al monto en UF a pagar por concepto de Bono precio
    bono_precio_promesa_uf = models.FloatField(verbose_name="Monto Bono Precio Promesa en UF",
                                               blank=True)  # Corresponde al 60% del Bono precio que se pagará por paso a promesa
    bono_precio_promesa_clp = models.FloatField(verbose_name="Monto Bono Precio Promesa en CLP",
                                                blank=True)  # Corresponde al 60% del Bono precio que se pagará por paso a promesa
    bono_precio_escritura_uf = models.FloatField(verbose_name="Monto Bono Precio esctitura en UF",
                                                 blank=True)  # Corresponde al 40% del Bono precio que se pagará por paso a escritura
    bono_precio_escritura_clp = models.FloatField(verbose_name="Monto Bono Precio Escritura en CLP",
                                                  blank=True)  # Corresponde al 40% del Bono precio que se pagará por paso a escritura
    monto_bono_c1 = models.FloatField(verbose_name="Monto Bono C1", blank=True)  # Corresponde al bono C1 de icp
    monto_bono_c2 = models.FloatField(verbose_name="Monto Bono C2", blank=True)  # Corresponde al bono C2 de icp
    monto_bono_c3 = models.FloatField(verbose_name="Monto Bono C3", blank=True)  # Corresponde al bono C3 de icp
    monto_desistimiento = models.FloatField(verbose_name="Monto Desistimiento", blank=True)
    total_comisiones = models.FloatField(verbose_name="Total Comisiones", blank=True)
    saldo_pagar = models.FloatField(verbose_name="Saldo a pagar del Total Comisiones", blank=True)
    total_bonos = models.FloatField(verbose_name="Total Bonos", blank=True)
    total_bonos_comisiones = models.FloatField(verbose_name="Total Bonos + Comisiones", blank=True)

    class Meta:
        db_table = "comisiones"


class Parametros_Comisione(models.Model):
    id_registro = models.AutoField(primary_key=True)
    periodo = models.ForeignKey(Cierre_Mes, verbose_name="Perido Cierre de mes", on_delete=models.CASCADE)
    id_asesor = models.CharField(verbose_name="Asesor", max_length=10)
    meta_venta = models.IntegerField(verbose_name="Meta de venta")
    venta_real = models.IntegerField(verbose_name="Venta real del periodo")
    renta_base = models.IntegerField(verbose_name="Renta base del periodo")
    porcentaje_cumplimiento = models.FloatField(verbose_name="Cumplimiento %")
    porcentaje_comision = models.FloatField(verbose_name="Porcentaje comisión")
    porcentaje_bono_precio = models.FloatField(verbose_name="Porcentaje Bono precio")

    class Meta:
        db_table = "parametros_comisiones"
