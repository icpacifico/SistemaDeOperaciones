from django.urls import path # Importar el path
# Importar las vistas de views
from .views import CrearCondominio,ListadoCondominio,ActualizarCondominio,CrearEtapa,ListadoEtapa,ActualizarEtapa,CrearTorre,ListadoTorre,ActualizarTorre,CrearModelo,ListadoModelo,ActualizarModelo,CrearBodega,ListadoBodega,ActualizarBodega,CrearEstacionamiento,ListadoEstacionamiento,ActualizarEstacionamiento,CrearVivienda,ListadoVivienda,ActualizarVivienda
from django.contrib.auth.decorators import login_required # Importar Login Regired para proteccion de urls


urlpatterns = [
    # Condominio
    path('crear_condominio/', login_required(CrearCondominio.as_view()), name='crear_condominio'),
    path('listar_condominio/', login_required(ListadoCondominio.as_view()), name='listar_condominio'),
    path('editar_condominio/<int:pk>/', login_required(ActualizarCondominio.as_view()), name='editar_condominio'),
    #path('eliminar_condominio/<int:pk>/', login_required(EliminarCondominio.as_view()), name='eliminar_condominio'),

    # Etapa
    path('crear_etapa/', login_required(CrearEtapa.as_view()), name='crear_etapa'),
    path('listar_etapa/', login_required(ListadoEtapa.as_view()), name='listar_etapa'),
    path('editar_etapa/<int:pk>/', login_required(ActualizarEtapa.as_view()), name='editar_etapa'),
    #path('eliminar_etapa/<int:pk>/', login_required(EliminarEtapa.as_view()), name='eliminar_etapa'),

    # Torre
    path('crear_torre/', login_required(CrearTorre.as_view()), name='crear_torre'),
    path('listar_torre/', login_required(ListadoTorre.as_view()), name='listar_torre'),
    path('editar_torre/<int:pk>/', login_required(ActualizarTorre.as_view()), name='editar_torre'),
    #path('eliminar_torre/<int:pk>/', login_required(EliminarTorre.as_view()), name='eliminar_torre'),

    # Modelo
    path('crear_modelo/', login_required(CrearModelo.as_view()), name='crear_modelo'),
    path('listar_modelo/', login_required(ListadoModelo.as_view()), name='listar_modelo'),
    path('editar_modelo/<int:pk>/', login_required(ActualizarModelo.as_view()), name='editar_modelo'),
    #path('eliminar_modelo/<int:pk>/', login_required(EliminarModelo.as_view()), name='eliminar_modelo'),

    # Bodega
    path('crear_bodega/', login_required(CrearBodega.as_view()), name='crear_bodega'),
    path('listar_bodega/', login_required(ListadoBodega.as_view()), name='listar_bodega'),
    path('editar_bodega/<int:pk>/', login_required(ActualizarBodega.as_view()), name='editar_bodega'),
    #path('eliminar_bodega/<int:pk>/', login_required(EliminarBodega.as_view()), name='eliminar_bodega'),

    # Estacionamiento
    path('crear_estacionamiento/', login_required(CrearEstacionamiento.as_view()), name='crear_estacionamiento'),
    path('listar_estacionamiento/', login_required(ListadoEstacionamiento.as_view()), name='listar_estacionamiento'),
    path('editar_estacionamiento/<int:pk>/', login_required(ActualizarEstacionamiento.as_view()), name='editar_estacionamiento'),
    #path('eliminar_estacionamiento/<int:pk>/', login_required(EliminarEstacionamiento.as_view()), name='eliminar_estacionamiento'),

    # Vivienda
    path('crear_vivienda/', login_required(CrearVivienda.as_view()), name='crear_vivienda'),
    path('listar_vivienda/', login_required(ListadoVivienda.as_view()), name='listar_vivienda'),
    path('editar_vivienda/<int:pk>/', login_required(ActualizarVivienda.as_view()), name='editar_vivienda'),
    #path('eliminar_vivienda/<int:pk>/', login_required(EliminarVivienda.as_view()), name='eliminar_vivienda'),
]