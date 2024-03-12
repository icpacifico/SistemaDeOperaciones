from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from .models import Cliente, Cotizacion, Venta, TipoDesistimiento, Desistimiento, Reserva
from .forms import ClienteForm, CotizacionForm, VentaForm, TipoDesistimientoForm, DesistimientoForm
from Contabilidad.forms import PagoForm
from Contabilidad.models import Pago
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime

# Create your views here.


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


class CrearCotizacion(CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = "ventas/gui_cotizacion/crear_cotizacion.html"  # Reemplaza "tu_app" con el nombre de tu aplicación
    success_url = reverse_lazy(
        "ventas:listar_cotizacion")  # Reemplaza "tu_app" y "listar_cotizaciones" con tus nombres de aplicación y URL


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
    datos =  Venta.objects.filter(id_venta=id_venta)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Guardar el pago en la base de datos si el formulario es válido
            pago = form.save()
            # Puedes redirigir a una página de detalles del pago, por ejemplo
            return redirect('contabilidad/gui_pagos/listar_pago.html')
    else:
        form = PagoForm()

    return render(request, 'contabilidad/gui_pagos/crear_pago.html', {'form': form, 'id_venta':id_venta, 'datos':datos})


def listado_detalle_venta(request, id_venta):
    datos =  Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request,'contabilidad/gui_pagos/listar_pago.html', {'datos':datos, 'id_venta':id_venta} )


def informe_pagos_venta(request,id_venta):
    datos =  Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'contabilidad/gui_pagos/detalle_pago.html', {'datos':datos, 'id_venta':id_venta, 'datos_venta':datos_venta})

def informe_pagos_venta_print(request,id_venta):
    datos =  Pago.objects.filter(id_venta=id_venta)
    datos_venta = Venta.objects.filter(id_venta=id_venta)
    return render(request, 'contabilidad/gui_pagos/detalle_pago_print.html', {'datos':datos, 'id_venta':id_venta, 'datos_venta':datos_venta})


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
            context = {'datos':datos, 'id_venta':self.kwargs['id_venta'], 'datos_venta':datos_venta, 'icon':'static/assets/img/illustrations/logo-horizontal.gif'}
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
def carta_cierre_negocios_venta(request,id_venta): # ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    pass


def entrega_documentos_venta(request,id_venta):# ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    pass


def despacho_promesa_venta(request,id_venta):# ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    pass


def carta_oferta_venta(request,id_venta):# ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    pass


def fpm_venta(request,id_venta):# ESTA VISTA ES PARA GENERAR UN DOCUMENTO
    pass


def desistir_venta(request,id_venta):# ESTA VISTA ES PARA CAMBIAR EL ESTADO DE LA VENTA A DESISTIMIENTO
    pass

def pasar_reserva(request, id_cotizacion):
    # datos_venta = Venta.objects.filter(id_venta=id_venta)
    # cotizacion_no = datos_venta.id_cotizacion
    datos_cotizacion= Cotizacion.objects.filter(id_cotizacon=id_cotizacion)
    cliente_id = datos_cotizacion.id_cliente
    datos_cliente = Cotizacion.objects.filter(id_cliente=cliente_id)
    datos_reserva = Reserva.objects.all()
    recibo =len(datos_reserva)+1

    nueva_reserva = Reserva(negocio=id_cotizacion,
                            referencia = datos_cotizacion.id_cotizacion,
                            fecha_creacion=datetime.now(),
                            fecha_aprovacion="",
                            cliente = str(datos_cliente.id_cliente.nombre_cliente+" "+datos_cliente.id_cliente.apellido_paterno_cliente),
                            no_recibo = recibo,
                            fono=datos_cliente.fono_cliente,
                            correo=datos_cliente.correo_cliente,
                            proyecto = "DV",
                            estado_reserva = "Pendiente")
    nueva_reserva.save()
    """ACÁ FALTARÍA CREAR EL CODIGO PARA LA CREACIÓN DE LA VENTA EN PARALELO A LA RESERVA
    TOMANDO TODOS LOS DATOS DE LA COTIZACIÓN Y CALCULANDO LOS DEMÁS ATRIBUTOS DEL MODELO DE VENTAS"""
    return ()

