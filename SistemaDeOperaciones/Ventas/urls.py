from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CrearCliente, ListadoClientes, ActualizarCliente,
    CrearCotizacion, ListadoCotizaciones, ActualizarCotizacion,
    CrearVenta, ListadoVentas, ActualizarVenta,
    CrearTipoDesistimiento, ListarTiposDesistimiento, ActualizarTipoDesistimiento,
    CrearDesistimiento, ListarDesistimientos, ActualizarDesistimiento,
    ListarReservas, detalle_reserva,
    detalle_venta, registrar_pago_venta,
    listado_detalle_venta, informe_pagos_venta, informe_pagos_venta_print, PagosInvoicePdf, carta_cierre_negocios_venta,
    entrega_documentos_venta, despacho_promesa_venta, carta_oferta_venta, fpm_venta)

app_name = 'ventas'

urlpatterns = [
    # Clientes
    path('crear_cliente/', login_required(CrearCliente.as_view()), name='crear_cliente'),
    path('listar_cliente/', login_required(ListadoClientes.as_view()), name='listar_cliente'),
    path('editar_cliente/<int:pk>/', login_required(ActualizarCliente.as_view()), name='editar_cliente'),

    # Cotizaciones
    path('crear_cotizacion/', login_required(CrearCotizacion.as_view()), name='crear_cotizacion'),
    path('listar_cotizacion/', login_required(ListadoCotizaciones.as_view()), name='listar_cotizacion'),
    path('editar_cotizacion/<int:pk>/', login_required(ActualizarCotizacion.as_view()), name='editar_cotizacion'),

    # Ventas
    path('crear_venta/', login_required(CrearVenta.as_view()), name='crear_venta'),
    path('listar_venta/', login_required(ListadoVentas.as_view()), name='listar_venta'),
    path('editar_venta/<int:pk>/', login_required(ActualizarVenta.as_view()), name='editar_venta'),
    path('detalle_venta/<int:id_venta>/', login_required(detalle_venta), name='detalle_venta'),
    path('crear_pago/<int:id_venta>/', login_required(registrar_pago_venta), name='crear_pago'),
    # listado_detalle_venta
    path('detalle_pagos/<int:id_venta>/', login_required(listado_detalle_venta), name='detalle_pagos'),
    path('informe_pagos/<int:id_venta>/', login_required(informe_pagos_venta), name='informe_pagos'),
    path('informe_pagos_print/<int:id_venta>/', login_required(informe_pagos_venta_print), name='informe_pagos_print'),
    path('pagos_invoice_pdf/<int:id_venta>/', login_required(PagosInvoicePdf.as_view()), name='pagos_invoice_pdf'),
    path('ccn/<int:id_venta>/', login_required(carta_cierre_negocios_venta), name='ccn'),
    path('entrega_docven/<int:id_venta>/', login_required(entrega_documentos_venta), name='entrega_docven'),
    path('desp_promesa/<int:id_venta>/', login_required(despacho_promesa_venta), name='desp_promesa'),
    path('co_ven/<int:id_venta>/', login_required(carta_oferta_venta), name='co_ven'),
    path('fpm_venta/<int:id_venta>/', login_required(fpm_venta), name='fpm_venta'),

    # Tipos de Desistimiento
    path('crear_tipodesistimiento/', login_required(CrearTipoDesistimiento.as_view()), name='crear_tipodesistimiento'),
    path('listar_tipodesistimiento/', login_required(ListarTiposDesistimiento.as_view()),
         name='listar_tipodesistimiento'),
    path('editar_tipodesistimiento/<int:pk>/', login_required(ActualizarTipoDesistimiento.as_view()),
         name='editar_tipodesistimiento'),

    # Desistimientos
    path('crear_desistimiento/', login_required(CrearDesistimiento.as_view()), name='crear_desistimiento'),
    path('listar_desistimiento/', login_required(ListarDesistimientos.as_view()), name='listar_desistimiento'),
    path('editar_desistimiento/<int:pk>/', login_required(ActualizarDesistimiento.as_view()),
         name='editar_desistimiento'),

    # Reservas
    path('listar_reserva/', login_required(ListarReservas.as_view()), name='listar_reserva'),
    path('detalle_reserva/<int:id_reserva>/', login_required(detalle_reserva), name='detalle_reserva'),

]
