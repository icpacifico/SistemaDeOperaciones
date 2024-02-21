from django.urls import path # Importar el path
# Importar las vistas de views
from .views import *
from django.contrib.auth.decorators import login_required # Importar Login Regired para proteccion de urls


urlpatterns = [
    # Nacionalidad
    path('crear_nacionalidad/', login_required(CrearNacionalidad.as_view()), name = 'crear_nacionalidad'),
    path('listar_nacionalidad/', login_required(ListadoNacionalidad.as_view()), name = 'listar_nacionalidad'),
    path('editar_nacionalidad/<int:pk>', login_required(ActualizarNacionalidad.as_view()), name = 'editar_nacionalidad'),

    # Banco
    path('crear_banco/', login_required(CrearBanco.as_view()), name='crear_banco'),
    path('listar_banco/', login_required(ListadoBanco.as_view()), name='listar_banco'),
    path('editar_banco/<int:pk>', login_required(ActualizarBanco.as_view()), name='editar_banco'),

    # ConjuntoParametros
    path('crear_parametros/', login_required(CrearConjuntoParametros.as_view()), name='crear_parametros'),
    path('listar_parametros/', login_required(ListadoConjuntoParametros.as_view()), name='listar_parametros'),
    path('editar_parametros/<int:pk>', login_required(ActualizarConjuntoParametros.as_view()), name='editar_parametros'),

    # Profesion
    path('crear_profesion/', login_required(CrearProfesion.as_view()), name='crear_profesion'),
    path('listar_profesion/', login_required(ListadoProfesion.as_view()), name='listar_profesion'),
    path('editar_profesion/<int:pk>', login_required(ActualizarProfesion.as_view()), name='editar_profesion'),

    # Usuarios
    # path('crear_profesion/', login_required(CrearProfesion.as_view()), name='crear_profesion'),
    path('listar_usuario/', login_required(ListadoUsuario.as_view()), name='listar_usuario'),
    # path('editar_profesion/<int:pk>', login_required(ActualizarProfesion.as_view()), name='editar_profesion'),

]