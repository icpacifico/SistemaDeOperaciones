from django.db import models
from Proyectos.models import Condominio
from SistemaDeOperaciones.funciones import validate_positive_integer
# Create your models here.
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key=True)
    nombre_nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50, null=False,blank=False)

    def __str__(self):
        return "("+str(self.id_nacionalidad)+")" + " " +self.nombre_nacionalidad

    class Meta:
        db_table = "nacionalidad"

class Banco(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco =  models.CharField(verbose_name="Banco", max_length=50, null=False,blank=False)
    def __str__(self):
        return "("+str(self.id_banco)+")" + " " +self.nombre_banco

    class Meta:
        db_table = "banco"


class ConjuntoParametros(models.Model):
    id_conjunto_parametros = models.AutoField(primary_key=True)
    id_condominio = models.ForeignKey(Condominio, verbose_name="Condominio", on_delete=models.CASCADE)
    factor_vendedor = models.IntegerField(verbose_name="Factor", validators =[validate_positive_integer], null=False,blank=False)
    precio_dcto_depto = models.FloatField(verbose_name="Precio descuento Depto", validators =[validate_positive_integer], null=False,blank=False)
    bono_precio_porce = models.IntegerField(verbose_name="Porcentaje Bono Precio", validators =[validate_positive_integer], null=False,blank=False)
    porcen_promesa = models.FloatField(verbose_name="Porcentaje Promesa", validators =[validate_positive_integer], null=False,blank=False)
    porcen_escritura = models.FloatField(verbose_name="Porcentaje Escritura", validators =[validate_positive_integer], null=False,blank=False)
    porcen_comision_vendedor = models.FloatField(verbose_name="% comisión Vendedor", validators =[validate_positive_integer], null=False,blank=False)
    monto_escrt_operaciones = models.IntegerField(verbose_name="Monto Escritura Operaciones (UF)", validators =[validate_positive_integer], null=False,blank=False)
    monto_reserva = models.IntegerField(verbose_name="Monto Reserva (UF)", validators =[validate_positive_integer], null=False,blank=False)
    monto_prorrateo = models.IntegerField(verbose_name="Monto a Prorratear", validators =[validate_positive_integer], null=False,blank=False)
    monto_recuperar = models.IntegerField(verbose_name="Monto a  Recuperar", validators =[validate_positive_integer], null=False,blank=False)
    fecha_recuperacion = models.DateField(verbose_name="Fecha Recuperación", null=False,blank=False)
    valor_bodega = models.IntegerField(verbose_name="$ Bodega", validators =[validate_positive_integer], null=False,blank=False)
    valor_estacionamiento = models.IntegerField(verbose_name="$ Estacionamiento", validators =[validate_positive_integer], null=False,blank=False)
    fecha_termino_venta = models.DateField(verbose_name="Fecha termino de ventas", validators =[validate_positive_integer], null=False,blank=False)
    direccion_condominio = models.CharField(max_length=100, verbose_name="Dirección Condominio", null=False,blank=False)
    banco_alzante = models.ForeignKey(Banco, verbose_name="Banco Alzante", on_delete=models.CASCADE, null=False,blank=False)

    def __str__(self):
        return "("+str(self.id_conjunto_parametros)+")" + " " +self.id_condominio.nombre_condominio

    class Meta:
        db_table = "parametros"


class Profesion(models.Model):
    id_profesion = models.AutoField(primary_key=True)
    nombre_profesion = models.CharField(verbose_name="Profesion",max_length=50, null=False,blank=False)

    def __str__(self):
        return "("+str(self.id_profesion)+")"+" - "+self.nombre_profesion

    class Meta:
        db_table = "profesion"
