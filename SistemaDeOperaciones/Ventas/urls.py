from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    CrearCliente, ListadoClientes, ActualizarCliente,
    CrearCotizacion, ListadoCotizaciones, ActualizarCotizacion,
    CrearVenta, ListadoVentas, ActualizarVenta,
    CrearTipoDesistimiento, ListarTiposDesistimiento, ActualizarTipoDesistimiento,
    CrearDesistimiento, ListarDesistimientos, ActualizarDesistimiento,detalle_venta, registrar_pago_venta,
    listado_detalle_venta
)

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

    # Tipos de Desistimiento
    path('crear_tipodesistimiento/', login_required(CrearTipoDesistimiento.as_view()), name='crear_tipodesistimiento'),
    path('listar_tipodesistimiento/', login_required(ListarTiposDesistimiento.as_view()), name='listar_tipodesistimiento'),
    path('editar_tipodesistimiento/<int:pk>/', login_required(ActualizarTipoDesistimiento.as_view()), name='editar_tipodesistimiento'),

    # Desistimientos
    path('crear_desistimiento/', login_required(CrearDesistimiento.as_view()), name='crear_desistimiento'),
    path('listar_desistimiento/', login_required(ListarDesistimientos.as_view()), name='listar_desistimiento'),
    path('editar_desistimiento/<int:pk>/', login_required(ActualizarDesistimiento.as_view()), name='editar_desistimiento'),
]
