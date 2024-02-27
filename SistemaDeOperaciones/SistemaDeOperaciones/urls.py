"""
URL configuration for SistemaDeOperaciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Administracion.views import logoutUsuario, Login, Inicio
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(Inicio.as_view()),name='index'),
    path('administracion/', include(('Administracion.urls', 'administracion'))),
    path('proyectos/', include(('Proyectos.urls', 'proyectos'))),
    path('ventas/', include(('Ventas.urls', 'ventas'))),
    path('accounts/login/', Login.as_view(template_name="pages/login.html"), name='login'),
 
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('admin/', admin.site.urls),
]
