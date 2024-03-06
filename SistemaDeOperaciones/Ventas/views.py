from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Cliente, Cotizacion, Venta, TipoDesistimiento, Desistimiento
from .forms import ClienteForm, CotizacionForm, VentaForm, TipoDesistimientoForm, DesistimientoForm
from Contabilidad.forms import PagoForm
from Contabilidad.models import Pago

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

def carta_cierre_negocios_venta(request):
    pass


def entrega_documentos_venta(request):
    pass


def despacho_promesa_venta(request):
    pass


def carta_oferta_venta(request):
    pass


def fpm_venta(request):
    pass


def desistir_venta(request):
    pass
