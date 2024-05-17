from django.db import models


class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey()
    id_vendedor =  models.CharField(max_length=10)
    condominio = models.CharField(max_length=10)
    etapa = models.CharField(max_length=10)
    torre = models.CharField(max_length=10)
    vivienda = models.CharField(max_length=10)
    bodega = models.CharField(max_length=10)
    estacionamiento = models.CharField(max_length=10)
    fecha_cotizacion = models.DateField()
    porcentaje_credito = models.FloatField()
    canal_cotizacion = models.CharField(verbose_name="Canal Cotización", max_length=200,
                                        choices=CANAL_COTIZACION_CHOICES, default=None)
    renta_cotizacion = models.CharField(verbose_name="Renta Cotización", max_length=200,
                                        choices=RENTA_COTIZACION_CHOICES, default=None)
    estado_cotizacion = models.CharField(verbose_name="Renta Cotización", max_length=200, choices=IS_ACTIVE_CHOICES,
                                         default=None)
    preaprobacion_cotizacion = models.CharField(verbose_name="Preaprobación Cotización", max_length=200,
                                                choices=PREAPROBACION_COTIZACION_CHOICES, default=None)

    pass


def invocar_desistimiento(request, id_venta):
    if request.method == 'POST':
        form = DesistimientoForm(request.POST)
        if form.is_valid():
            form.save()
            # Cambiar el estado de la venta a desistimeinto
            venta = get_object_or_404(Venta, id_venta=id_venta)
            venta.estado_ven = 'Desestimiento'
            venta.save()
            # Obetener la vivienda de la venta
            id_vivienda = Venta.objects.values_list('id_vivienda').filter(id_venta=id_venta)
            id_vivienda = id_vivienda[0][0]
            # Cambiar el estado de la vivienda a disponible
            vivienda = get_object_or_404(Vivienda, id_vivienda=id_vivienda)
            vivienda.estado_vivienda = 'Disponible'
            vivienda.save()
            # Cambiar el estado de la bodega a disponible
            bodega = get_object_or_404(Bodega, id_vivienda=id_vivienda)
            bodega.estado_bodega = 'bodega'
            bodega.save()
            # Cambiar el estado del estacionamiento disponible
            est = get_object_or_404(Estacionamiento, id_vivienda=id_vivienda)
            est.estado_estacionamiento = 'Disponible'
            est.save()
            return redirect('ventas:listar_desistimiento')  # Cambiar a la URL correcta
    else:
        form = DesistimientoForm(initial={'id_venta': id_venta})  # Pasar el valor inicial al formulario
    return render(request, 'ventas/gui_desistimientos/crear_desistimiento_2.html', {'id_venta': id_venta, 'form': form})



