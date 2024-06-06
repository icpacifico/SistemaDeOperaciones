from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CrearCliente, ListadoClientes, ActualizarCliente,
    CrearCotizacion, ListadoCotizaciones, ActualizarCotizacion,ver_cotizacion_pdf ,CotizacionPdf,
    CrearVenta, ListadoVentas, ActualizarVenta,
    CrearTipoDesistimiento, ListarTiposDesistimiento, ActualizarTipoDesistimiento,
    CrearDesistimiento, ListarDesistimientos, ActualizarDesistimiento,
    pasar_reserva, ListarReservas, detalle_reserva,anular_reserva,
    detalle_venta, registrar_pago_venta,
    listado_detalle_venta, informe_pagos_venta, PagosInvoicePdf, CierreNegociopdf,
    carta_cierre_negocios_venta, entrega_documentos_venta, EntregaDocumentoPdf, despacho_promesa_venta,
    Despacho_promesa_ventaPdf, carta_oferta_venta, Carta_oferta_ventaPdf, generate_excel, fpm_venta, Fpm_VentaPdf,
    invocar_desistimiento)

app_name = 'ventas'

urlpatterns = [
    # Clientes
    path('crear_cliente/', login_required(CrearCliente.as_view()), name='crear_cliente'),
    path('listar_cliente/', login_required(ListadoClientes.as_view()), name='listar_cliente'),
    path('editar_cliente/<str:pk>/', login_required(ActualizarCliente.as_view()), name='editar_cliente'),

    # Cotizaciones
    path('crear_cotizacion/', login_required(CrearCotizacion.as_view()), name='crear_cotizacion'),
    path('listar_cotizacion/', login_required(ListadoCotizaciones.as_view()), name='listar_cotizacion'),
    path('editar_cotizacion/<int:pk>/', login_required(ActualizarCotizacion.as_view()), name='editar_cotizacion'),
    path('print_cotizacion/<int:id_cotizacion>/', login_required(CotizacionPdf.as_view()), name='print_cotizacion'),
    path('ver_cotizacion_pdf/<int:id_cotizacion>/', login_required(ver_cotizacion_pdf), name='ver_cotizacion_pdf'),

    # Ventas
    path('crear_venta/', login_required(CrearVenta.as_view()), name='crear_venta'),
    path('listar_venta/', login_required(ListadoVentas.as_view()), name='listar_venta'),
    path('editar_venta/<int:pk>/', login_required(ActualizarVenta.as_view()), name='editar_venta'),
    path('detalle_venta/<int:id_venta>/', login_required(detalle_venta), name='detalle_venta'),
    path('crear_pago/<int:id_venta>/', login_required(registrar_pago_venta), name='crear_pago'),
    # listado_detalle_venta
    path('detalle_pagos/<int:id_venta>/', login_required(listado_detalle_venta), name='detalle_pagos'),
    path('informe_pagos/<int:id_venta>/', login_required(informe_pagos_venta), name='informe_pagos'),
    # path('informe_pagos_print/<int:id_venta>/', login_required(informe_pagos_venta_print), name='informe_pagos_print'),
    path('pagos_invoice_pdf/<int:id_venta>/', login_required(PagosInvoicePdf.as_view()), name='pagos_invoice_pdf'),
    path('ccn/<int:id_venta>/', login_required(carta_cierre_negocios_venta), name='ccn'),
    path('ccn_print/<int:id_venta>/', login_required(CierreNegociopdf.as_view()), name='ccn_print'),
    path('entrega_docven/<int:id_venta>/', login_required(entrega_documentos_venta), name='entrega_docven'),
    path('entrega_docven_print/<int:id_venta>/', login_required(EntregaDocumentoPdf.as_view()),
         name='entrega_docven_print'),
    path('desp_promesa/<int:id_venta>/', login_required(despacho_promesa_venta), name='desp_promesa'),
    path('desp_promesa_print/<int:id_venta>/', login_required(Despacho_promesa_ventaPdf.as_view()),
         name='desp_promesa_print'),
    path('co_ven/<int:id_venta>/', login_required(carta_oferta_venta), name='co_ven'),
    path('co_ven_print/<int:id_venta>/', login_required(Carta_oferta_ventaPdf.as_view()), name='co_ven_print'),
    path('co_ven_excel/<int:id_venta>/', login_required(generate_excel), name='co_ven_excel'),
    path('fpm_venta/<int:id_venta>/', login_required(fpm_venta), name='fpm_venta'),
    path('fpm_venta_print/<int:id_venta>/', login_required(Fpm_VentaPdf.as_view()), name='fpm_venta_print'),

    # Tipos de Desistimiento
    path('crear_tipodesistimiento/', login_required(CrearTipoDesistimiento.as_view()), name='crear_tipodesistimiento'),
    path('listar_tipodesistimiento/', login_required(ListarTiposDesistimiento.as_view()),
         name='listar_tipodesistimiento'),
    path('editar_tipodesistimiento/<int:pk>/', login_required(ActualizarTipoDesistimiento.as_view()),
         name='editar_tipodesistimiento'),

    # Desistimientos
    path('call_desist/<int:id_venta>/', login_required(invocar_desistimiento), name='call_desist'),
    path('crear_desistimiento/', login_required(CrearDesistimiento.as_view()), name='crear_desistimiento'),
    path('listar_desistimiento/', login_required(ListarDesistimientos.as_view()), name='listar_desistimiento'),
    path('editar_desistimiento/<int:pk>/', login_required(ActualizarDesistimiento.as_view()),
         name='editar_desistimiento'),

    # Reservas
    path('pasar_reserva/<int:id_cotizacion>/', login_required(pasar_reserva), name='pasar_reserva'),
    path('listar_reserva/', login_required(ListarReservas.as_view()), name='listar_reserva'),
    path('detalle_reserva/<int:id_reserva>/', login_required(detalle_reserva), name='detalle_reserva'),
    path('anular_reserva/<int:id_reserva>/', login_required(anular_reserva), name='anular_reserva'),

    # Promesas
    path('pasar_reserva/<int:id_cotizacion>/', login_required(pasar_reserva), name='pasar_reserva'),

]
