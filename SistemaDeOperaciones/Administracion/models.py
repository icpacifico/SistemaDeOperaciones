from django.db import models
from Proyectos.models import Condominio
# Create your models here.
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField()
    nombre_nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return str("("+self.id_nacionalidad+")") + " " +self.nombre_nacionalidad

    class Meta:
        db_table = "nacionalidad"

class Banco(models.Model):
    id_banco = models.AutoField()
    nombre_banco =  models.CharField(max_length=50)
    def __str__(self):
        return str("("+self.id_banco+")") + " " +self.nombre_banco

    class Meta:
        db_table = "banco"

class ConjuntoParametros(model.Model):
    id_conjunto_parametros = models.AutoField(primary_key=True)
    id_condominio = models.ForeignKey(Condominio, verbose_name="Condominio", on_delete=models.CASCADE)
    factor_junior_vendedor = models.IntegerField(verbose_name="Factor")
    factor_advance_vendedor = models.FloatField(verbose_name="Factor")
    factor_senior_vendedor = models.FloatField(verbose_name="Factor")
    precio_dcto_depto = models.FloatField(verbose_name="Precio descuento Depto")
    bono_precio_porce = models.IntegerField(verbose_name="Porcentaje Bono Precio")
    porcen_promesa = models.FloatField(verbose_name="Porcentaje Promesa")
    porcen_escritura = models.FloatField(verbose_name="Porcentaje Escritura")
    porcen_comision_vendedor = models.FloatField(verbose_name="% comisión Vendedor")
    porcen_comision_supervisor = models.FloatField(verbose_name="% comisión Supervisor")
    porcen_comision_jefeventas = models.FloatField(verbose_name="% comisión Jefe de Ventas")
    monto_escrt_operaciones = models.IntegerField(verbose_name="Monto Escritura Operaciones (UF)")
    monto_reserva = models.IntegerField(verbose_name="Monto Reserva (UF)")
    porcen_bono_precio_jefeventas = models.FloatField(verbose_name="% Bono precio Jefe Ventas")
    monto_prorrateo = models.IntegerField(verbose_name="Monto a Prorratear")
    porcen_bono_precio_supervisor = models.FloatField(verbose_name="% Bono precio SUpervisor")
    monto_recuperar = models.IntegerField(verbose_name="Monto a  Recuperar")
    fecha_recuperacion = models.DateField(verbose_name="Fecha Recuperación")
    valor_bodega = models.IntegerField(verbose_name="$ Bodega")
    valor_estacionamiento = models.IntegerField(verbose_name="$ Estacionamiento")
    factor_junior_jefeventas = models.IntegerField(verbose_name="Factor Junior Jefe Ventas")
    factor_advance_jefeventas = models.IntegerField(verbose_name="Factor Advance Jefe Ventas")
    factor_senior_jefeventas = models.IntegerField(verbose_name="Factor Senior Jefe Ventas")
    factor_junior_supervisor = models.IntegerField(verbose_name="Factor Junior Supervisor")
    factor_advance_supervisor = models.IntegerField(verbose_name="Factor Advance Supervisor")
    factor_senior_supervisor = models.IntegerField(verbose_name="Factor Senior Supervisor")
    fecha_termino_venta = models.DateField(verbose_name="Fecha termino de ventas")
    direccion_condominio = models.CharField(max_length=100, verbose_name="Dirección Condominio")
    banco_alzante = models.ForeignKey(Banco, verbose_name="Banco Alzante")

    def __str__(self):
        return str("("+self.id_conjunto_parametros+")") + " " +self.id_condominio.nombre_condominio

    class Meta:
        db_table = "parametros"