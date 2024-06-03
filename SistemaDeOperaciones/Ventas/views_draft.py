import pandas
import pandas as pd


def cotizacion_from_cliente(request, id_cliente):
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:listar_cotizacion')
    else:
        form = CotizacionForm(initial={'id_cliente': id_cliente})
    return render(request, 'ventas/gui_cotizacion/crear_cotizacion_from_cliente.html',
                  {'id_cliente': id_cliente, 'form': form})


class CotizacionPdf(View):
    # datos = Pago.objects.filter(id_venta=id_venta)
    # datos_venta = Venta.objects.filter(id_venta=id_venta)

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_URL  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise RuntimeError(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            # Extracción de los datos de la cotizacion
            """
            Por parametro solo nos llega el el id de la cotización que se quiere imprimir.
            - Desde la cotización debemos obtener los datos del cliente Model = Cliente
            - Desde la cotización debemos obtener los datos del la vivienda Model = Vivienda
            - Desde la Vivienda debemos obtener lo datos de las bodegas y los estacionamientos
            - Desde la Vivienda debemos obetener los datos del condominio
            - Desde la API de UF obtener el Valor de las UF
            - Desde la Cotización Obtener los datos del vendedor
            
            Calcular las formas de pago según los porcentajes de Reserva-Pie-Credito
            Calcular las simulaciones de los creditos Hipotecarios
            """

            # Datos del cliente
            datos_cliente = Cotizacion.objects.values_list('id_cliente').filter(
                id_cotizacion=self.kwars['id_cotizacion'])
            id_cliente = datos_cliente[0][0]
            datos_cliente = Cliente.objects.filter(id_cliente=id_cliente)
            # Datos de la vivienda
            datos_vivienda = Cotizacion.objects.values_list('id_vivienda').filter(
                id_cotizacion=self.kwars['id_cotizacion'])
            id_vivienda = datos_vivienda[0][0]
            datos_vivienda = Vivienda.objects.filter(id_vivienda=id_vivienda)
            # Datos de las bodegas
            datos_bodega = Bodega.objects.filter(id_vivienda=id_vivienda)
            # Datos de los Estacionamientos
            datos_estacionamiento = Estacionamiento.objects.filter(id_vivienda=id_vivienda)
            # Datos del condominio
            modelo = Vivienda.objects.values_list('id_modelo').filter(id_vivienda=id_vivienda)
            id_torre = Vivienda.objects.values_list('id_torre').filter(id_vivienda=id_vivienda)
            id_modelo = modelo[0][0]
            nombre_modelo = Modelo.objects.values_list('nombre_modelo').filter(id_modelo=id_modelo)
            nombre_modelo = nombre_modelo[0][0]
            id_torre = id_torre[0][0]
            nombre_torre = Torre.objects.values_list('nombre_torre').filter(id_torre=id_torre)
            nombre_torre = nombre_torre[0][0]
            id_etapa_condominio = Torre.objects.values_list('id_etapa_condominio').filter(id_torre=id_torre)
            id_etapa_condominio = id_etapa_condominio[0][0]
            nombre_etapa = Etapa.objects.values_list('nombre_etapa').filter(id_etapa_condominio=id_etapa_condominio)
            nombre_etapa = nombre_etapa[0][0]
            datos_modelo = Modelo.objects.values_list('id_condominio').filter(id_modelo=id_modelo)
            id_condominio = datos_modelo[0][0]
            datos_condominio = Condominio.objects.values_list('nombre_condominio').filter(id_condominio=id_condominio)
            nombre_condominio = datos_condominio[0][0]
            direccion_proyecto = Condominio.objects.values_list('direccion_proyecto').filter(
                id_condominio=id_condominio)
            direccion_proyecto = direccion_proyecto[0][0]
            datos_proyecto = {'condominio': nombre_condominio, 'etapa': nombre_etapa, 'torre': nombre_torre,
                              'direccion': direccion_proyecto}

            # Calculos de los valores de la cotización

            # Calculo de datos de los precios de la vivienda-bodega-estacionamiento
            uf = 35250
            valores_bienes = pd.Dataframe(colums['item', 'valor_uf', 'valor_clp'])
            valores_bienes.loc[0] = [datos_vivienda.nombre_vivienda, datos_vivienda.valor_vivienda,
                                     datos_vivienda.valor_vivienda * uf]
            valores_bienes.loc[1] = [datos_bodega.nombre_bodega, datos_bodega.valor_bodega,
                                     datos_bodega.valor_bodega * uf]
            valores_bienes.loc[2] = [datos_estacionamiento.nombre_estacionamiento,
                                     datos_estacionamiento.valor_estacionamiento,
                                     datos_estacionamiento.valor_estacionamiento * uf]

            # Usar un for para rellenar los calculos
            valores_bienes.loc[3] = ["Total Precio Lista",
                                     valores_bienes.iloc[0][1]+valores_bienes.iloc[1][1]+valores_bienes.iloc[2][1],
                                     valores_bienes.iloc[0][1]+valores_bienes.iloc[1][1]+valores_bienes.iloc[2][1]]
            valores_bienes.loc[4] = ["Descuentos",
                                     350,
                                     350 * uf]
            valores_bienes.loc[5] = ["Total Precio Venta",
                                     valores_bienes.iloc[3][1]-valores_bienes.iloc[4][1],
                                     valores_bienes.iloc[3][2]-valores_bienes.iloc[4][2]]

            # Calculo de Datos de la forma de pago
            # Usar un for para los calculos de las formas de pago
            porcentaje_credito = 80
            reserva = 10
            porcentaje_pie = 100-porcentaje_credito-reserva
            porcentaje_reserva = reserva/valores_bienes.iloc[0][1]
            valor_pie_uf = porcentaje_pie*datos_vivienda.valor_vivienda
            valor_credito_uf = porcentaje_credito*datos_vivienda.valor_vivienda
            total_en_uf = porcentaje_credito, reserva+valor_pie_uf+valor_credito_uf
            forma_pago =  pd.Dataframe(columns['concepto', 'porcentaje', 'valor_uf', 'valor_clp'])
            forma_pago.loc[0] = ['Reserva', porcentaje_reserva, reserva, reserva*uf]
            forma_pago.loc[1] = ['Pie Contado', porcentaje_pie, valor_pie_uf, valor_pie_uf*uf]
            forma_pago.loc[2] = ['Credito Hipotecario', porcentaje_credito, valor_credito_uf, valor_credito_uf * uf]
            forma_pago.loc[3] = ['Total', porcentaje_reserva+porcentaje_pie+total_en_uf, total_en_uf * uf]
            # Calculo de Datos de la sumulación de Credito Hipotecario

            tasa_anual = 4
            simulacion_credito = pd.DataFrame(columns['Plazo en años', 'Tasa Anual (%)', 'UF', '$CLP', 'Renta Requerida'])
            simulacion_credito.loc[0] = [15, tasa_anual, "", "", ""]
            simulacion_credito.loc[1] = [20, tasa_anual, "", "", ""]
            simulacion_credito.loc[2] = [25, tasa_anual, "", "", ""]
            simulacion_credito.loc[3] = [30, tasa_anual, "", "", ""]
            # Usar un For para los calculos de la simulación del credito hipotecario


            # Template que se renderiza para obtener el PDF
            template = get_template('ventas/gui_cotizacion/crear_cotizacion_from_cliente.html')
            # Diccionaro context para entregar los datos  al template que se renderiza
            context = {'viviendas': datos_vivienda, 'clientes': datos_cliente, 'bodegas': datos_bodega,
                       'estacionamientos': datos_estacionamiento, 'proyectos': datos_proyecto,
                       'icon': 'static/assets/img/illustrations/logo-horizontal.gif'}

            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback)
            return response
        except:
            pass
        return HttpResponseRedirect(request, 'ventas/gui_cotizacion/listar_cotizacion.html')


def anular_reserva(request, id_reserva):
    reserva = Reserva.objects.get(id_reserva= id_reserva)
    reserva.estado_reserva = "Anulada"
    reserva.save()
    cotizacion =  Reserva.objects.values_list('referencia').filter(id_reserva=id_reserva)
    cotizacion = cotizacion[0][0]
    mod_cot =  Cotizacion.objects.get(id_cotizacion = cotizacion)
    mod_cot.estado_cotizacion ="Anulada"
    mod_cot.save()
    vivienda = Cotizacion.objects.values_list('id_vivienda').filter(id_cotizacion = cotizacion)
    vivienda =  vivienda[0][0]
    mod_viv = Vivienda.objects.get(id_vivienda=vivienda)
    mod_viv.estado_vivienda = "Disponible"
    mod_viv.save()
    bodega = Bodega.objects.values_list('id_bodega').filter(id_vivienda = vivienda)
    bodega = bodega[0][0]
    mod_bod = Bodega.objects.get(id_bodega = bodega)
    mod_bod.estado_bodega = "Disponible"
    mod_bod.save()
    estacionamiento = Estacionamiento.objects.values_list('id_estacionamiento').filter(id_vivienda = vivienda)
    estacionamiento = estacionamiento[0][0]
    mod_est = Estacionamiento.objects.get(id_estacionamiento=estacionamiento)
    mod_est.estado_estacionamiento = "Disponible"
    mod_est.save()

    return render(request, 'ventas/gui_reserva/listar_reserva.html')



def pasar_reserva(request, id_cotizacion):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    datos_cliente = Cotizacion.objects.values_list('id_cliente').filter(
        id_cotizacion=id_cotizacion)
    id_cliente = datos_cliente[0][0]
    datos_cliente = Cliente.objects.filter(id_cliente=id_cliente)
    # Datos de la vivienda
    datos_vivienda = Cotizacion.objects.values_list('id_vivienda').filter(
        id_cotizacion=id_cotizacion)
    id_vivienda = datos_vivienda[0][0]
    datos_vivienda = Vivienda.objects.filter(id_vivienda=id_vivienda)
    # Datos de las bodegas
    datos_bodega = Bodega.objects.filter(id_vivienda=id_vivienda)
    # Datos de los Estacionamientos
    datos_estacionamiento = Estacionamiento.objects.filter(id_vivienda=id_vivienda)
    # Datos del condominio
    modelo = Vivienda.objects.values_list('id_modelo').filter(id_vivienda=id_vivienda)
    id_torre = Vivienda.objects.values_list('id_torre').filter(id_vivienda=id_vivienda)
    id_modelo = modelo[0][0]
    nombre_modelo = Modelo.objects.values_list('nombre_modelo').filter(id_modelo=id_modelo)
    nombre_modelo = nombre_modelo[0][0]
    id_torre = id_torre[0][0]
    nombre_torre = Torre.objects.values_list('nombre_torre').filter(id_torre=id_torre)
    nombre_torre = nombre_torre[0][0]
    id_etapa_condominio = Torre.objects.values_list('id_etapa_condominio').filter(id_torre=id_torre)
    id_etapa_condominio = id_etapa_condominio[0][0]
    nombre_etapa = Etapa.objects.values_list('nombre_etapa').filter(id_etapa_condominio=id_etapa_condominio)
    nombre_etapa = nombre_etapa[0][0]
    datos_modelo = Modelo.objects.values_list('id_condominio').filter(id_modelo=id_modelo)
    id_condominio = datos_modelo[0][0]
    datos_condominio = Condominio.objects.values_list('nombre_condominio').filter(id_condominio=id_condominio)
    nombre_condominio = datos_condominio[0][0]
    direccion_proyecto = Condominio.objects.values_list('direccion_proyecto').filter(
        id_condominio=id_condominio)
    direccion_proyecto = direccion_proyecto[0][0]
    datos_proyecto = {'condominio': nombre_condominio, 'etapa': nombre_etapa, 'torre': nombre_torre,
                      'direccion': direccion_proyecto}


    return render(request, 'ventas/gui_reserva/crear_reserva.html',
                  {'viviendas': datos_vivienda, 'clientes': datos_cliente, 'bodegas': datos_bodega,
                   'estacionamientos': datos_estacionamiento, 'proyectos': datos_proyecto,
                   'id_cotizacion': id_cotizacion})



def registrar_pago_venta(request, id_venta):
    datos = Venta.objects.filter(id_venta=id_venta)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Guardar el pago en la base de datos si el formulario es válido
            pago = form.save()
            # Puedes redirigir a una página de detalles del pago, por ejemplo
            return redirect('contabilidad/gui_pagos/listar_pago.html')
    else:
        form = PagoForm()

    return render(request, 'contabilidad/gui_pagos/crear_pago.html',
                  {'form': form, 'id_venta': id_venta, 'datos': datos})