from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from .models import Cliente, Cotizacion, Venta, TipoDesistimiento, Desistimiento, Reserva, Condominio, Etapa, Torre, \
    Vivienda
from Proyectos.models import Modelo, Bodega, Estacionamiento
from .forms import ClienteForm, CotizacionForm, VentaForm, TipoDesistimientoForm, DesistimientoForm
from Contabilidad.forms import PagoForm
from Contabilidad.models import Pago, Banco
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime
from django.http import JsonResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter
from xlsxwriter.workbook import Workbook
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import json


# Create your views here.

def get_etapas(request):
    condominio_id = request.GET.get('condominio_id')
    etapas = Etapa.objects.filter(id_condominio=condominio_id)
    data = [{'id_etapa_condominio': etapa.id_etapa_condominio, 'nombre_etapa': etapa.nombre_etapa} for etapa in etapas]
    return JsonResponse(data, safe=False)


def get_torres(request):
    etapa_id = request.GET.get('etapa_id')
    torres = Torre.objects.filter(id_etapa_condominio=etapa_id)
    data = [{'id_torre': torre.id_torre, 'nombre_torre': torre.nombre_torre} for torre in torres]
    return JsonResponse(data, safe=False)


def get_viviendas(request):
    torre_id = request.GET.get('torre_id')
    viviendas = Vivienda.objects.filter(id_torre=torre_id)
    data = [{'id_vivienda': vivienda.id_vivienda, 'nombre_vivienda': vivienda.nombre_vivienda} for vivienda in
            viviendas]
    return JsonResponse(data, safe=False)


class CrearCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "ventas/gui_cliente/crear_cliente.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_cliente")  # Reemplaza "tu_app" y "listar_clientes" con tus nombres de aplicación y URL


class ListadoClientes(ListView):
    model = Cliente
    template_name = "ventas/gui_cliente/listar_cliente.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "clientes"
    queryset = Cliente.objects.all()


class ActualizarCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "ventas/gui_cliente/crear_cliente.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_cliente")  # Reemplaza "tu_app" y "listar_clientes" con tus nombres de aplicación y URL


def crear_cotizacion(request):
    if request.method == 'POST':
        # Extraer los valores del QueryDict
        id_condominio = request.POST.get('id_condominio')
        id_etapa = request.POST.get('id_etapa')
        id_torre = request.POST.get('id_torre')
        id_vivienda = request.POST.get('id_vivienda')
        id_vivienda = int(id_vivienda)
        id_vivienda = Vivienda.objects.get(id_vivienda=id_vivienda)
        id_cliente = request.POST.get('id_cliente')
        id_cliente = str(id_cliente)
        id_cliente = Cliente.objects.get(id_cliente=id_cliente)
        procentaje_credito_cotizacion = request.POST.get('procentaje_credito_cotizacion')
        canal_cotizacion = request.POST.get('canal_cotizacion')
        renta_cotizacion = request.POST.get('renta_cotizacion')
        coti = Cotizacion(
            id_vivienda=id_vivienda,
            id_cliente=id_cliente,
            procentaje_credito_cotizacion=procentaje_credito_cotizacion,
            canal_cotizacion=canal_cotizacion,
            renta_cotizacion=renta_cotizacion,
        )
        coti.save()
        return redirect(reverse_lazy('ventas:listar_cotizacion'))  # Reemplaza con tu URL de éxito
    else:
        form = CotizacionForm()

    # Añadir contexto adicional
    context = {
        'form': form,
        'clientes': Cliente.objects.all(),
        'condominios': Condominio.objects.values_list('id_condominio', 'nombre_condominio')
    }

    return render(request, 'ventas/gui_cotizacion/crear_cotizacion.html', context)


def cotizacion_from_cliente(request, id_cliente):
    pass


class ListadoCotizaciones(ListView):
    model = Cotizacion
    template_name = "ventas/gui_cotizacion/listar_cotizacion.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "cotizaciones"
    queryset = Cotizacion.objects.all()


class ActualizarCotizacion(UpdateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = "ventas/gui_cotizacion/crear_cotizacion.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_cotizacion")  # Reemplaza "tu_app" y "listar_cotizaciones" con tus nombres de aplicación y URL


class CrearVenta(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = "ventas/gui_venta/crear_venta.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_venta")  # Reemplaza "tu_app" y "listar_ventas" con tus nombres de aplicación y URL


class ListadoVentas(ListView):
    model = Venta
    template_name = "ventas/gui_venta/listar_venta.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "ventas"
    queryset = Venta.objects.all()


class ActualizarVenta(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = "ventas/gui_venta/crear_venta.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_venta")  # Reemplaza "tu_app" y "listar_ventas" con tus nombres de aplicación y URL


class CrearTipoDesistimiento(CreateView):
    model = TipoDesistimiento
    form_class = TipoDesistimientoForm
    template_name = "ventas/gui_desistimientos/crear_tipodesistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_tipodesistimiento")  # Reemplaza "tu_app" y "listar_tipos_desistimiento" con tus nombres de aplicación y URL


class ListarTiposDesistimiento(ListView):
    model = TipoDesistimiento
    template_name = "ventas/gui_desistimientos/listar_tipodesistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "tipos_desistimiento"
    queryset = TipoDesistimiento.objects.all()


class ActualizarTipoDesistimiento(UpdateView):
    model = TipoDesistimiento
    form_class = TipoDesistimientoForm
    template_name = "ventas/gui_desistimientos/crear_tipodesistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_tipodesistimiento")  # Reemplaza "tu_app" y "listar_tipos_desistimiento" con tus nombres de aplicación y URL


class CrearDesistimiento(CreateView):
    model = Desistimiento
    form_class = DesistimientoForm
    template_name = "ventas/gui_desistimientos/crear_desistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_desistimiento")  # Reemplaza "tu_app" y "listar_desistimientos" con tus nombres de aplicación y URL


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


def crear_desistimiento(request, id_venta):
    pass


class ListarDesistimientos(ListView):
    model = Desistimiento
    template_name = "ventas/gui_desistimientos/listar_desistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "desistimientos"
    queryset = Desistimiento.objects.all()


class ActualizarDesistimiento(UpdateView):
    model = Desistimiento
    form_class = DesistimientoForm
    template_name = "ventas/gui_desistimientos/crear_desistimiento.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_desistimiento")  # Reemplaza "tu_app" y "listar_desistimientos" con tus nombres de aplicación y URL


class ListarReservas(ListView):
    model = Reserva
    template_name = "ventas/gui_reserva/listar_reserva.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    context_object_name = "reservas"
    queryset = Reserva.objects.all()


def detalle_reserva(request, id_reserva):
    detalle = get_object_or_404(Reserva, id_reserva=id_reserva)
    return render(request, 'ventas/gui_reserva/detalle_reserva.html', {'detalle': detalle})


# Acciones de Ventas

def detalle_venta(request, id_venta):
    venta = get_object_or_404(Venta, id_venta=id_venta)
    return render(request, 'ventas/gui_venta/detalle_venta.html', {'venta': venta})


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


def listado_detalle_venta(request, id_venta):
    datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'contabilidad/gui_pagos/listar_pago.html', {'datos': datos, 'id_venta': id_venta})


def informe_pagos_venta(request, id_venta):
    datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'contabilidad/gui_pagos/detalle_pago.html',
                  {'datos': datos, 'id_venta': id_venta, 'datos_venta': datos_venta})


class PagosInvoicePdf(View):
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
            datos = Pago.objects.filter(id_venta=self.kwargs['id_venta'])
            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])
            template = get_template('contabilidad/gui_pagos/prueba_pdf.html')
            context = {'datos': datos, 'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
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
        return HttpResponseRedirect(request, 'ventas/gui_venta/listar_venta.html')


def carta_cierre_negocios_venta(request, id_venta):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    datos_cierre_negocio = Pago.objects.filter(id_venta=id_venta,
                                               categoria_pago='cierre_negocio')
    # Datos de Detalle Pie
    datos_detalle_pie = Pago.objects.filter(id_venta=id_venta, categoria_pago='detalle_pie')

    return render(request, 'documentos/carta_cierre_negocio.html',
                  {'datos_venta': datos_venta, 'datos_detalle_pie': datos_detalle_pie, 'id_venta': id_venta,
                   'datos_venta': datos_venta})


class CierreNegociopdf(View):
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
            # Datos de cierre de negocio
            datos_cierre_negocio = Pago.objects.filter(id_venta=self.kwargs['id_venta'],
                                                       categoria_pago='cierre_negocio')
            # Datos de Detalle Pie
            datos_detalle_pie = Pago.objects.filter(id_venta=self.kwargs['id_venta'], categoria_pago='detalle_pie')

            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])
            template = get_template('documentos/carta_cierre_negocio_print.html')
            context = {'datos_cierre_negocio': datos_cierre_negocio, 'datos_detalle_pie': datos_detalle_pie,
                       'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
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
        return HttpResponseRedirect(reverse_lazy("ventas:listar_venta"))


def entrega_documentos_venta(request, id_venta):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'documentos/entrega_documentos.html',
                  {'datos': datos, 'id_venta': id_venta, 'datos_venta': datos_venta})


class EntregaDocumentoPdf(View):
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
            datos = Pago.objects.filter(id_venta=self.kwargs['id_venta'])
            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])

            template = get_template('documentos/entrega_documentos_print.html')
            context = {'datos': datos, 'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
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
        return HttpResponseRedirect(reverse_lazy("ventas:listar_venta"))


def despacho_promesa_venta(request, id_venta):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    # datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'documentos/despacho_promesa.html',
                  {'id_venta': id_venta, 'datos_venta': datos_venta})


class Despacho_promesa_ventaPdf(View):
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
            print("Entra al TRY")
            datos = Pago.objects.filter(id_venta=self.kwargs['id_venta'])
            print("Obtiene los datos ", datos)
            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])
            print("Obtiene los datos de la venta ", datos_venta)
            template = get_template('documentos/despacho_promesa_print.html')
            print("Obtiene el template que se va a renderizar", template)

            context = {'datos': datos, 'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
                       'icon': 'static/assets/img/illustrations/logo-horizontal.gif'}
            print("Se obtiene el contexto que se enviará", context)

            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            print("Se crea el response ", response)

            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback)
            print("Crea el pisa_status ", pisa_status)

            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy("ventas:listar_venta"))


def carta_oferta_venta(request, id_venta):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    # datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    id_cotización = Venta.objects.values_list('id_cotizacion').filter(id_venta=id_venta)
    id_cotizacion = id_cotización[0][0]
    id_vivienda = Cotizacion.objects.values_list('id_vivienda').filter(id_cotizacion=id_cotizacion)
    id_vivienda = id_vivienda[0][0]
    datos_bodega = Bodega.objects.filter(id_vivienda=id_vivienda)
    datos_estacionamiento = Estacionamiento.objects.filter(id_vivienda=id_vivienda)

    return render(request, 'documentos/carta_oferta.html',
                  {'id_venta': id_venta, 'datos_venta': datos_venta, 'datos_bodega': datos_bodega,
                   'datos_estacionamiento': datos_estacionamiento, })


class Carta_oferta_ventaPdf(View):
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
            print("Entra al TRY")
            datos = Pago.objects.filter(id_venta=self.kwargs['id_venta'])
            print("Obtiene los datos ", datos)
            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])
            print("Obtiene los datos de la venta ", datos_venta)
            id_cotización = Venta.objects.values_list('id_cotizacion').filter(id_venta=self.kwargs['id_venta'])
            id_cotizacion = id_cotización[0][0]
            id_vivienda = Cotizacion.objects.values_list('id_vivienda').filter(id_cotizacion=id_cotizacion)
            id_vivienda = id_vivienda[0][0]
            datos_bodega = Bodega.objects.filter(id_vivienda=id_vivienda)
            datos_estacionamiento = Estacionamiento.objects.filter(id_vivienda=id_vivienda)
            template = get_template('documentos/carta_oferta_print.html')
            print("Obtiene el template que se va a renderizar", template)
            context = {'datos': datos, 'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
                       'datos_bodega': datos_bodega,
                       'datos_estacionamiento': datos_estacionamiento,
                       'icon': 'static/assets/img/illustrations/logo-horizontal.gif'}
            print("Se obtiene el contexto que se enviará", context)
            html = template.render(context)
            # print("Se crea la variable html ", html)
            response = HttpResponse(content_type='application/pdf')
            print("Se crea el response ", response)
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback)
            print("Crea el pisa_status ", pisa_status)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy("ventas:listar_venta"))


def generate_excel(request, id_venta):
    # Buscar los datos de la sección "Datos Carta de Oferta"
    datos_venta = Venta.objects.values_list('id_cotizacion').filter(id_venta=id_venta)
    id_cotizacion = datos_venta[0][0]
    datos_cotizacion = Cotizacion.objects.values_list('id_cliente').filter(id_cotizacion=id_cotizacion)
    id_cliente = datos_cotizacion[0][0]
    nombre_cliente = Cliente.objects.values_list('nombre_cliente').filter(id_cliente=id_cliente)
    nombre2_cliente = Cliente.objects.values_list('nombre2_cliente').filter(id_cliente=id_cliente)
    apellido_paterno_cliente = Cliente.objects.values_list('apellido_paterno_cliente').filter(id_cliente=id_cliente)
    apellido_materno_cliente = Cliente.objects.values_list('apellido_materno_cliente').filter(id_cliente=id_cliente)
    nombre_cliente = nombre_cliente[0][0]
    nombre2_cliente = nombre2_cliente[0][0]
    apellido_paterno_cliente = apellido_paterno_cliente[0][0]
    apellido_materno_cliente = apellido_materno_cliente[0][0]
    rut_cliente = id_cliente
    cliente = nombre_cliente + " " + nombre2_cliente + " " + apellido_paterno_cliente + " " + apellido_materno_cliente
    print(cliente)

    # Buscar los datos de la sección "Datos del Proyecto"
    datos_cotizacion = Cotizacion.objects.values_list('id_vivienda').filter(id_cotizacion=id_cotizacion)
    id_vivienda = datos_cotizacion[0][0]
    datos_vivienda = Vivienda.objects.values_list('id_modelo').filter(id_vivienda=id_vivienda)
    id_torre = Vivienda.objects.values_list('id_torre').filter(id_vivienda=id_vivienda)
    id_modelo = datos_vivienda[0][0]
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
    direccion_proyecto = Condominio.objects.values_list('direccion_proyecto').filter(id_condominio=id_condominio)
    direccion_proyecto = direccion_proyecto[0][0]
    vivienda_social = Condominio.objects.values_list('vivienda_social').filter(id_condominio=id_condominio)
    vivienda_social = vivienda_social[0][0]

    # Buscar los datos de la sección "Datos Inmueble"
    nombre_vivienda = Vivienda.objects.values_list('nombre_vivienda').filter(id_vivienda=id_vivienda)
    nombre_vivienda = nombre_vivienda[0][0]
    valor_vivienda = Vivienda.objects.values_list('valor_vivienda').filter(id_vivienda=id_vivienda)
    valor_vivienda = str(valor_vivienda[0][0]) + " UF"
    pie_real_ven = Venta.objects.values_list('pie_real_ven').filter(id_venta=id_venta)
    pie_real_ven = str(pie_real_ven[0][0]) + " UF"
    ahorro_previo = Venta.objects.values_list('ahorro_previo').filter(id_venta=id_venta)
    ahorro_previo = str(ahorro_previo[0][0]) + " UF"
    monto_subsidio = Venta.objects.values_list('monto_subsidio').filter(id_venta=id_venta)
    monto_subsidio = str(monto_subsidio[0][0]) + " UF"
    monto_credito_real_ven = Venta.objects.values_list('monto_credito_real_ven').filter(id_venta=id_venta)
    monto_credito_real_ven = str(monto_credito_real_ven[0][0]) + " UF"
    rol_vivienda = Vivienda.objects.values_list('rol_vivienda').filter(id_vivienda=id_vivienda)
    rol_vivienda = rol_vivienda[0][0]
    nombre_bodega = Bodega.objects.values_list('nombre_bodega').filter(id_vivienda=id_vivienda)
    nombre_bodega = nombre_bodega[0][0]
    valor_bodega = Bodega.objects.values_list('valor_bodega').filter(id_vivienda=id_vivienda)
    valor_bodega = str(valor_bodega[0][0]) + " UF"
    rol_bodega = Bodega.objects.values_list('rol_bodega').filter(id_vivienda=id_vivienda)
    rol_bodega = rol_bodega[0][0]
    nombre_estacionamiento = Estacionamiento.objects.values_list('nombre_estacionamiento').filter(
        id_vivienda=id_vivienda)
    nombre_estacionamiento = nombre_estacionamiento[0][0]
    valor_estacionamiento = Estacionamiento.objects.values_list('valor_estacionamiento').filter(id_vivienda=id_vivienda)
    valor_estacionamiento = str(valor_estacionamiento[0][0]) + " UF"
    """rol_bodega = Bodega.objects.values_list('rol_bodega').filter(id_vivienda=id_vivienda)
    rol_bodega = rol_bodega[0][0]"""
    rol_estacionamiento = "1234-4321"

    # Crear un objeto BytesIO para almacenar el archivo Excel en memoria
    output = BytesIO()

    # Crear un nuevo libro de trabajo
    workbook = Workbook(output, {'in_memory': True})

    # Añadir una hoja de cálculo
    worksheet = workbook.add_worksheet("Carta de Oferta")

    # Definir un rango de 6 columnas y 27 filas
    num_rows = 9
    num_cols = 6
    start_row = 1
    start_col = 0

    # Crear un formato con bordes negros
    border_format = workbook.add_format({'border': 1})  # 1 para un borde fino

    # Aplicar el formato con bordes a todas las celdas dentro del rango de A1 a F27
    worksheet.conditional_format('A1:F27', {'type': 'no_blanks', 'format': border_format})

    # Crear un formato con el color de fondo gris claro
    grey_light_format = workbook.add_format({'bg_color': '#D3D3D3'})  # Código hexadecimal para gris claro

    # Crear un nuevo formato basado en el formato existente pero con el color de fondo verde claro
    green_light_format = workbook.add_format()
    green_light_format.set_bold(True)
    green_light_format.set_font_size(12)
    green_light_format.set_align('center')
    green_light_format.set_bg_color('#C9FFC1')  # Código hexadecimal para verde claro
    green_light_format.set_border(3)

    # Combinar celdas A1:F1 para el título
    worksheet.merge_range('A1:F1', 'Datos Carta Oferta', green_light_format)

    # Escribir datos en el rango de celdas
    # Escribir los conceptos originales en las celdas A2:A10
    original_concepts = ['Nombre del Titular', 'Rut', 'Razón Social Inmobiliaria', 'Rut',
                         'Quien Cancela Gastos Operacionales', 'En Que Notaria Firma Escritura',
                         'Banco Alzante',
                         'Banco a Depositar', 'Cta Corriente N°']
    datos_carta_oferta = [cliente, id_cliente, "Inmobiliaria Costanera Pacífico SpA", "76.866.075-1", cliente,
                          "Notaria de Don Pepito", "Banco Security", 'Banco a Depositar', 'Cta Corriente N°']
    for i, concept in enumerate(original_concepts):
        worksheet.write(i + start_row, start_col, concept, grey_light_format)

    # Combinar celdas B2:F10 para la descripción de los conceptos originales
    for row in range(start_row, start_row + num_rows):
        worksheet.merge_range(row, start_col + 1, row, start_col + num_cols - 1,
                              f'{datos_carta_oferta[row - start_row]}',
                              workbook.add_format({'align': 'left'}))

    # Combinar celdas A11:F11 para agregar una separación
    worksheet.merge_range('A11:F11', ' ', workbook.add_format({'align': 'center'}))

    # Combinar celdas A12:F12 para agregar un segundo título
    worksheet.merge_range('A12:F12', 'Datos Del Proyecto', green_light_format)

    # Escribir datos en el rango de celdas para los nuevos conceptos (A13:A18)
    new_concepts = ['Proyecto', 'Etapa', 'Torre', 'Modelo', 'Dirección Inmueble',
                    'Vivienda Social']
    datos_proyecto = [nombre_condominio, nombre_etapa, nombre_torre, nombre_modelo, direccion_proyecto, vivienda_social]
    for i, concept in enumerate(new_concepts):
        worksheet.write(i + 12, 0, concept, grey_light_format)

    # Combinar celdas B13:F18 para la descripción de los nuevos conceptos
    for row in range(12, 18):
        worksheet.merge_range(row, 1, row, 5,
                              f'{datos_proyecto[row - 12]}', workbook.add_format({'align': 'left'}))

    # Combinar celdas A19:F19 para agregar una separación
    worksheet.merge_range('A19:F19', 'Nota: Bodega con USO y GOCE ', workbook.add_format({'align': 'center'}))

    # Combinar celdas A20:F20 para agregar un nuevo título con el formato modificado
    worksheet.merge_range('A20:F20', 'Datos Inmueble', green_light_format)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (A21:A23)
    additional_concepts = ['NRO. DEPARTAMENTO Y/O CASA', 'NRO. ESTACIONAMIENTO', 'NRO. BODEGA']
    for i, concept in enumerate(additional_concepts):
        worksheet.write(i + 20, 0, concept, grey_light_format)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (A21:A23)
    num_bienes = [nombre_vivienda, nombre_estacionamiento, nombre_bodega]
    for i, concept in enumerate(num_bienes):
        worksheet.write(i + 20, 1, concept)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (C21:C23)
    additional_concepts = ['UF Depto. o Casa', 'UF Estacionamiento.', 'UF Bodega']
    for i, concept in enumerate(additional_concepts):
        worksheet.write(i + 20, 2, concept, grey_light_format)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (C21:C23)
    precio_bienes = [valor_vivienda, valor_estacionamiento, valor_bodega]
    for i, concept in enumerate(precio_bienes):
        worksheet.write(i + 20, 3, concept)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (E21:E23)
    additional_concepts = ['ROL', 'ROL', 'ROL']
    for i, concept in enumerate(additional_concepts):
        worksheet.write(i + 20, 4, concept, grey_light_format)

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (E21:E23)
    roles_bienes = [rol_vivienda, rol_estacionamiento, rol_bodega]
    for i, concept in enumerate(roles_bienes):
        worksheet.write(i + 20, 5, concept)

    # Combinar celdas A24:F24 para agregar una separación
    worksheet.merge_range('A24:F24', ' ', workbook.add_format({'align': 'center'}))

    # Escribir datos en el rango de celdas para los nuevos conceptos adicionales (A25:D25)
    additional_concepts = ['Precio Venta', 'RECURSOS PROPIOS(PIE)', 'SUBSIDIO', 'AHORRO PREVIO']
    valores_venta = [valor_vivienda, pie_real_ven, monto_subsidio, ahorro_previo]
    for i, concept in enumerate(additional_concepts):
        worksheet.write(24, i + 0, concept, grey_light_format)

    # Combinar celdas E25:F25 para agregar el concepto de Monto Credito
    # worksheet.merge_range('E25:F25', 'Monto Credito',grey_light_format, workbook.add_format({'align': 'center'}))
    # Crear un formato con el color de fondo gris claro
    grey_light_format = workbook.add_format({'bg_color': '#D3D3D3'})  # Código hexadecimal para gris claro

    # Combinar celdas E25:F25 para agregar el concepto de Monto Credito con el color de fondo gris claro
    worksheet.merge_range('E25:F25', 'Monto Crédito', grey_light_format)
    # Combinar celdas E26:F26 para agregar El monto del Credito
    worksheet.merge_range('E26:F26', monto_credito_real_ven, workbook.add_format({'align': 'center'}))

    # Agregar el concepto de Observación en la celda A27
    worksheet.write(26, 0, "Observaciones", grey_light_format)

    # Combinar celdas B27:F27 para agregar la observación
    worksheet.merge_range('B27:F27', 'Proyecto Afecto a IVA, incluido en el precio.',
                          workbook.add_format({'align': 'left'}))

    # Cerrar el libro de trabajo
    workbook.close()

    # Volver al principio del objeto BytesIO
    output.seek(0)

    # Crear una respuesta HTTP con el contenido del archivo Excel
    response = HttpResponse(output.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Establecer el encabezado para que el navegador descargue el archivo en lugar de mostrarlo
    response['Content-Disposition'] = 'attachment; filename=Carta_Oferta.xlsx'

    return response


def fpm_venta(request, id_venta):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    # datos = Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'documentos/fpm.html',
                  {'id_venta': id_venta, 'datos_venta': datos_venta})


class Fpm_VentaPdf(View):
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
            datos = Pago.objects.filter(id_venta=self.kwargs['id_venta'])
            datos_venta = Venta.objects.filter(id_venta=self.kwargs['id_venta'])

            template = get_template('documentos/fpm_print.html')
            context = {'datos': datos, 'id_venta': self.kwargs['id_venta'], 'datos_venta': datos_venta,
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
        return HttpResponseRedirect(reverse_lazy("ventas:listar_venta"))


@csrf_exempt
def pasar_reserva(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
    cliente = get_object_or_404(Cliente, id_cliente=cotizacion.id_cliente.id_cliente)
    vivienda = get_object_or_404(Vivienda, id_vivienda=cotizacion.id_vivienda.id_vivienda)

    nombre_cliente = f"{cliente.nombre_cliente} {cliente.apellido_paterno_cliente} {cliente.apellido_materno_cliente}"
    fono_cliente = cliente.fono_cliente
    correo_cliente = cliente.correo_cliente

    bodega = Bodega.objects.filter(id_vivienda=vivienda.id_vivienda)
    estacionamiento = Estacionamiento.objects.filter(id_vivienda=vivienda.id_vivienda)

    modelo = vivienda.id_modelo
    torre = vivienda.id_torre
    etapa = torre.id_etapa_condominio
    condominio = modelo.id_condominio

    datos_proyecto = {
        'condominio': condominio.nombre_condominio,
        'etapa': etapa.nombre_etapa,
        'torre': torre.nombre_torre,
        'direccion': condominio.direccion_proyecto
    }

    if request.method == 'POST':
        print("Ha ingresado al método POST")

        # Verificar el cuerpo de la solicitud
        print("Contenido de request.body:", request.body)

        try:
            pagos_data = json.loads(request.body).get('pagos', [])
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Error al decodificar JSON', 'details': str(e)},
                                status=400)

        print("Datos de pagos recibidos:", pagos_data)

        nueva_reserva = Reserva(
            negocio=id_cotizacion,
            referencia=id_cotizacion,
            fecha_creacion=datetime.now(),
            fecha_aprobacion=datetime.now(),
            cliente=cliente,
            no_recibo=Reserva.objects.count() + 1,
            fono=fono_cliente,
            correo=correo_cliente,
            proyecto=condominio.nombre_condominio,
            estado_reserva="Pendiente"
        )
        nueva_reserva.save()
        # Obtener el ID de la nueva reserva
        id_nueva_reserva = nueva_reserva.id_reserva
        # CAMBIO DE ESTADOS DE LA COTIZACIÓN, Y BIENES
        cotizacion_update = get_object_or_404(Cotizacion, id_cotizacion=id_cotizacion)
        cotizacion_update.estado_cotizacion = 'En Reserva'
        cotizacion_update.save()
        vivienda_update = get_object_or_404(Vivienda, id_vivienda=cotizacion.id_vivienda.id_vivienda)
        vivienda_update.estado_vivienda = 'No Disponible'
        vivienda_update.save()
        bodega = get_object_or_404(Bodega, id_vivienda_id=vivienda_update.id_vivienda)
        bodega.estado_bodega = 'No Disponible'
        bodega.save()
        estacionamiento_update = get_object_or_404(Estacionamiento, id_vivienda_id=vivienda_update.id_vivienda)
        estacionamiento_update.estado_estacionamiento = 'No Disponible'
        estacionamiento_update.save()

        for conjunto in pagos_data:
            # La variable conjunto contiene los datos de los pagos de la reserva que se quiere registrar
            # Accediendo a los valores
            csrf_token = conjunto['csrfmiddlewaretoken']
            forma_pago = conjunto['forma_pago']
            id_banco = conjunto['id_banco']
            id_banco = int(id_banco)
            banco = Banco.objects.get(id_banco=id_banco)
            print("tipo de variable banco ", type(banco))
            fecha_pago = conjunto['fecha_pago']
            monto_pago = conjunto['monto_pago']
            print("creación nuevo pago")
            nuevo_pago = Pago(
                forma_pago=forma_pago,
                id_reserva=id_nueva_reserva,
                id_banco=banco,
                categoria_pago='cierre_negocio',
                estado_pago='pendiente',
                fecha_pago=fecha_pago,
                fecha_real_pago=fecha_pago,
                monto_pago=monto_pago,
                descripcion="Pago de reserva"
            )
            # print(nuevo_pago)
            print("Nuevo pago creado")
            nuevo_pago.save()

        return JsonResponse({'status': 'success'}, status=201)


    else:
        form = PagoForm()
        context = {
            'viviendas': [vivienda],
            'clientes': [cliente],
            'bodegas': bodega,
            'estacionamientos': estacionamiento,
            'proyectos': datos_proyecto,
            'id_cotizacion': id_cotizacion,
            'form': form
        }

        return render(request, 'ventas/gui_reserva/crear_reserva.html', context)


def pasar_promesa(request, referencia):
    # CALCULOS DEL MODELO DE VENTAS

    cotizacion = get_object_or_404(Cotizacion, id_cotizacion=referencia)
    cliente = get_object_or_404(Cliente, id_cliente=cotizacion.id_cliente.id_cliente)
    vivienda = get_object_or_404(Vivienda, id_vivienda=cotizacion.id_vivienda.id_vivienda)

    precio_vivienda = Vivienda.objects.values_list('valor_vivienda').filter(
        id_vivienda=cotizacion.id_vivienda.id_vivienda)
    precio_vivienda = precio_vivienda[0][0]
    print(type(precio_vivienda))
    print(precio_vivienda)

    nombre_cliente = f"{cliente.nombre_cliente} {cliente.apellido_paterno_cliente} {cliente.apellido_materno_cliente}"
    fono_cliente = cliente.fono_cliente
    correo_cliente = cliente.correo_cliente

    bodega = Bodega.objects.filter(id_vivienda=vivienda.id_vivienda)
    estacionamiento = Estacionamiento.objects.filter(id_vivienda=vivienda.id_vivienda)

    modelo = vivienda.id_modelo
    torre = vivienda.id_torre
    etapa = torre.id_etapa_condominio
    condominio = modelo.id_condominio

    datos_proyecto = {
        'condominio': condominio.nombre_condominio,
        'etapa': etapa.nombre_etapa,
        'torre': torre.nombre_torre,
        'direccion': condominio.direccion_proyecto
    }

    if request.method == 'POST':
        print("Ha ingresado al método POST ####")

        # Verificar el cuerpo de la solicitud
        print("Contenido de request.body:", request.body)

        try:
            pagos_data = json.loads(request.body).get('pagos', [])

            body_unicode = request.body.decode('utf-8')

            # Convertir la cadena JSON a un diccionario de Python
            body_data = json.loads(body_unicode)

            # Extraer los datos de promesa
            promesa_data = body_data.get('promesa', [])

            csrf_token_promesa = promesa_data['csrfmiddlewaretoken']
            print(csrf_token_promesa)
            fecha_ven = promesa_data['fecha_ven']
            print(fecha_ven)
            forma_pago_promesa = promesa_data['forma_pago']
            print(forma_pago_promesa)
            pie_real_ven = promesa_data['pie_real_ven']
            pie_real_ven = int(pie_real_ven)
            print(pie_real_ven)
            valor_numerico = promesa_data['valor_numerico']
            print(valor_numerico)
            valor_numerico=int(valor_numerico)
            reserva = 10

            # Imprimir los datos de promesa (opcional, para depuración)
            print("Datos de Promesa:", promesa_data)

        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': 'Error al decodificar JSON', 'details': str(e)},
                                status=400)

        # NUEVA VENTA
        nueva_venta = Venta(
            monto_reserva_ven=reserva,
            descuento_manual_ven=valor_numerico,  # Descuento que le aplica a la venta
            descuento_precio_ven=valor_numerico,  # Descuento que tiene la vivienda por promoción
            descuento_adicional_ven=valor_numerico,  # Descuento extra de la venta
            descuento_ven=valor_numerico,  # Total descontado a la venta
            pie_cancelado_ven=0,  # Pie total que a cancelado el cliente - Se deben sumar los pagos
            pie_cobrar_ven=pie_real_ven,  # Pie restante por pagar
            monto_estacionamiento_ven=0,  # Monto del estacionamiento
            monto_bodega_ven=0,  # Monto de la bodega
            monto_vivienda_ven=precio_vivienda,  # Valor de la vivineda
            monto_vivienda_ingreso_ven=0,  # Monto total que le ingresa a la inmo por la venta
            monto_ven=precio_vivienda-valor_numerico,  # Valor de venta del depto
            factor_categoria_ven=0,  # Ni carajo  idea que es
            porcentaje_comision_ven=0,  # Calculo de la comisión de los vendedores
            promesa_porcentaje_comision_reparto_ven=0,  # calculo comisión % promesa 40%
            promesa_monto_comision_ven=0,  # monto en clp del % de la comisión X promesa
            escritura_porcentaje_comision_reparto_ven=0,  # calculo comisión % escritura 40%
            escritura_monto_comision_ven=0,  # monto en clp del % de la comisión X escritura
            total_comision_ven=0,  # total de la comisión del vendedor
            bono_vivienda_ven=0,  # Bono de venta
            porcentaje_bono_precio_ven=0,  # % de bono que se le da al vendendor
            promesa_bono_precio_ven=0,  # % distribuciíon
            escritura_bono_precio_ven=0,  # % de distribución
            total_bono_precio_ven=0,  # Bono total del vendedpor
            numero_compra_ven=0,  # ??
            cotizacion_ven=0,  # n° Cotización
            monto_credito_ven=precio_vivienda-valor_numerico-pie_real_ven-reserva,  # Monto credito que le da el banco
            monto_credito_real_ven=precio_vivienda-valor_numerico-pie_real_ven-reserva,  # Monto de credito entregado por el banco
            ahorro_previo=0,  # Ahorro del cliente
            monto_subsidio=0,  # Monto del subsidio del estado
            pie_real_ven=pie_real_ven,  # Pie real del cliente
            valor_factor_ven=0,
            pie_abono_ven="si",# ??
            tipo_pago = forma_pago_promesa,
            id_banco_id = 1,
            id_cotizacion_id =1,


        )
        nueva_venta.save()
        print("Venta registrada")
        # Obtener el ID de la nueva reserva
        id_nueva_venta = nueva_venta.id_venta

        
        # CAMBIO DE ESTADOS DE LA COTIZACIÓN, Y BIENES
        reserva_update = get_object_or_404(Reserva, referencia=referencia)
        reserva_update.estado_reserva = 'En Promesa'
        reserva_update.save()
       
        for conjunto in pagos_data:
        # La variable conjunto contiene los datos de los pagos de la reserva que se quiere registrar
        # Accediendo a los valores
            csrf_token = conjunto['csrfmiddlewaretoken']
            forma_pago = conjunto['forma_pago']
            id_banco = conjunto['id_banco']
            id_banco = int(id_banco)
            banco = Banco.objects.get(id_banco=id_banco)
            print("tipo de variable banco ", type(banco))
            fecha_pago = conjunto['fecha_pago']
            monto_pago = conjunto['monto_pago']
        nuevo_pago = Pago(
            forma_pago=forma_pago,
            id_venta=id_nueva_venta,
            id_banco=banco,
            categoria_pago='detalle_pie',
            estado_pago='pendiente',
            fecha_pago=fecha_pago,
            fecha_real_pago=fecha_pago,
            monto_pago=monto_pago,
            descripcion="Pago de Pie"
        )
        nuevo_pago.save()

        return JsonResponse({'status': 'success'}, status=201)



    else:
        form = PagoForm()
        form_venta = VentaForm()
        context = {
            'viviendas': [vivienda],
            'precio_vivienda': precio_vivienda,
            'clientes': [cliente],
            'bodegas': bodega,
            'estacionamientos': estacionamiento,
            'proyectos': datos_proyecto,
            'id_cotizacion': referencia,
            'form': form,
            'form_venta': form_venta
        }

        return render(request, 'ventas/gui_promesa/crear_promesa.html', context)


def anular_reserva(request, id_reserva):
    # agregar un correo automatico a contabibildiad con cc a operaciones, grenci de ventas indicando la devolución del dinero
    reserva = Reserva.objects.get(id_reserva=id_reserva)
    reserva.estado_reserva = "Anulada"
    reserva.save()
    cotizacion = Reserva.objects.values_list('referencia').filter(id_reserva=id_reserva)
    cotizacion = cotizacion[0][0]
    mod_cot = Cotizacion.objects.get(id_cotizacion=cotizacion)
    mod_cot.estado_cotizacion = "Anulada"
    mod_cot.save()
    vivienda = Cotizacion.objects.values_list('id_vivienda').filter(id_cotizacion=cotizacion)
    vivienda = vivienda[0][0]
    mod_viv = Vivienda.objects.get(id_vivienda=vivienda)
    mod_viv.estado_vivienda = "Disponible"
    mod_viv.save()
    bodega = Bodega.objects.values_list('id_bodega').filter(id_vivienda=vivienda)
    bodega = bodega[0][0]
    mod_bod = Bodega.objects.get(id_bodega=bodega)
    mod_bod.estado_bodega = "Disponible"
    mod_bod.save()
    estacionamiento = Estacionamiento.objects.values_list('id_estacionamiento').filter(id_vivienda=vivienda)
    estacionamiento = estacionamiento[0][0]
    mod_est = Estacionamiento.objects.get(id_estacionamiento=estacionamiento)
    mod_est.estado_estacionamiento = "Disponible"
    mod_est.save()
    reservas = Reserva.objects.all()

    return render(request, 'ventas/gui_reserva/listar_reserva.html', {'reservas': reservas})


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


def ver_cotizacion_pdf(request, id_cotizacion):  # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
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

    # Template que se renderiza para obtener el PDF
    template = get_template('documentos/cotizacion_print.html')
    # Diccionaro context para entregar los datos  al template que se renderiza
    context = {'viviendas': datos_vivienda, 'clientes': datos_cliente, 'bodegas': datos_bodega,
               'estacionamientos': datos_estacionamiento, 'proyectos': datos_proyecto,
               'icon': 'static/assets/img/illustrations/logo-horizontal.gif'}

    return render(request, 'documentos/cotizacion.html',
                  {'viviendas': datos_vivienda, 'clientes': datos_cliente, 'bodegas': datos_bodega,
                   'estacionamientos': datos_estacionamiento, 'proyectos': datos_proyecto,
                   'id_cotizacion': id_cotizacion})


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
        print("INGRESA AL GET")
        try:
            print("INGRESA AL TRY")
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
            n_cotizacion = self.kwargs['id_cotizacion']

            # Datos Cotización
            fecha_coti = Cotizacion.objects.values_list('fecha_cotizacion').filter(
                id_cotizacion=self.kwargs['id_cotizacion'])
            fecha_coti = fecha_coti[0][0]
            # Datos del cliente
            datos_cliente = Cotizacion.objects.values_list('id_cliente').filter(
                id_cotizacion=self.kwargs['id_cotizacion'])
            id_cliente = datos_cliente[0][0]
            datos_cliente = Cliente.objects.filter(id_cliente=id_cliente)
            # Datos de la vivienda
            datos_vivienda = Cotizacion.objects.values_list('id_vivienda').filter(
                id_cotizacion=self.kwargs['id_cotizacion'])
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

            # Template que se renderiza para obtener el PDF
            template = get_template('documentos/cotizacion_print.html')
            # Diccionaro context para entregar los datos  al template que se renderiza
            context = {'viviendas': datos_vivienda, 'clientes': datos_cliente, 'bodegas': datos_bodega,
                       'estacionamientos': datos_estacionamiento, 'proyectos': datos_proyecto,
                       'n_cotizacion': n_cotizacion, 'fecha_coti': fecha_coti,
                       'icon': 'static/assets/img/illustrations/logo-horizontal.gif'}
            html = template.render(context)

            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback)
            return response
        except Exception as e:
            print(e)
            pass
        return HttpResponseRedirect(reverse_lazy("ventas:listar_cotizacion"))
