from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, FormView, TemplateView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from Administracion.forms import FormularioLogin
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.forms import UserChangeForm

class Inicio(TemplateView):
    template_name = 'pages/index.html'

def reporte_comisiones(request):
    return render(request, 'administracion/reportes/reporte_comisiones.html')
class ListadoUsuario(ListView):
    model = User
    template_name = "administracion/gui_usuarios/listar_usuarios.html"
    context_object_name = "usuarios"
    queryset = User.objects.all()

class UserInfoView(DetailView):
    model = User
    template_name = 'administracion/gui_usuarios/perfil.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener el usuario
        usuario = context['usuario']

        # Obtener los grupos a los que pertenece el usuario
        grupos_usuario = usuario.groups.all()

        # Obtener los permisos directos del usuario
        permisos_directos = usuario.user_permissions.all()

        # Obtener los permisos a través de los grupos
        permisos_grupos = Permission.objects.filter(group__in=grupos_usuario)

        context['grupos'] = grupos_usuario
        context['permisos_directos'] = permisos_directos
        context['permisos_grupos'] = permisos_grupos

        return context

class Login(FormView):
    template_name = 'pages/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
 
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
 
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)
 
 
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')



# Vistas basadas en clases de Nacionalidad
class CrearNacionalidad(CreateView):
    model = Nacionalidad
    form_class = NacionalidadForm
    template_name = "administracion/gui_nacionalidad/crear_nacionalidad.html"
    success_url = reverse_lazy("administracion:listar_nacionalidad")
    def form_valid(self, form):
        nombre_nacionalidad = form.cleaned_data['nombre_nacionalidad']
        if Nacionalidad.objects.filter(nombre_nacionalidad=nombre_nacionalidad).exists():
            form.add_error('nombre_nacionalidad', 'Nacionalidad with this name already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)


class ListadoNacionalidad(ListView):
    model = Nacionalidad
    template_name = "administracion/gui_nacionalidad/listar_nacionalidad.html"
    context_object_name = "nacionalidades"
    queryset = Nacionalidad.objects.all()


class ActualizarNacionalidad(UpdateView):
    model = Nacionalidad
    form_class = NacionalidadForm
    template_name = "administracion/gui_nacionalidad/crear_nacionalidad.html"
    success_url = reverse_lazy("administracion:listar_nacionalidad")


# Vistas basadas en clases de Banco
class CrearBanco(CreateView):
    model = Banco
    form_class = BancoForm  # Asegúrate de tener el formulario correspondiente
    template_name = "administracion/gui_banco/crear_banco.html"
    success_url = reverse_lazy("administracion:listar_banco")
    def form_valid(self, form):
        nombre_banco = form.cleaned_data['nombre_banco']
        if Banco.objects.filter(nombre_banco=nombre_banco).exists():
            form.add_error('nombre_banco', 'Banco with this name already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)

class ListadoBanco(ListView):
    model = Banco
    template_name = "administracion/gui_banco/listar_banco.html"
    context_object_name = "bancos"  # Define el nombre del objeto en el contexto
    queryset = Banco.objects.all()


class ActualizarBanco(UpdateView):
    model = Banco
    form_class = BancoForm
    template_name = "administracion/gui_banco/crear_banco.html"
    success_url = reverse_lazy("administracion:listar_banco")



# Vistas basadas en clases de ConjuntoParametros
class CrearConjuntoParametros(CreateView):
    model = ConjuntoParametros
    form_class = ConjuntoParametrosForm
    template_name = "administracion/gui_parametros/crear_parametros.html"
    success_url = reverse_lazy("administracion:listar_parametros")


class ListadoConjuntoParametros(ListView):
    model = ConjuntoParametros
    template_name = "administracion/gui_parametros/listar_parametros.html"
    context_object_name = "parametros"
    queryset = ConjuntoParametros.objects.all()


class ActualizarConjuntoParametros(UpdateView):
    model = ConjuntoParametros
    form_class = ConjuntoParametrosForm
    template_name = "administracion/gui_parametros/crear_parametros.html"
    success_url = reverse_lazy("administracion:listar_parametros")



# Vistas basadas en clases de Profesion
class CrearProfesion(CreateView):
    model = Profesion
    form_class = ProfesionForm
    template_name = "administracion/gui_profesion/crear_profesion.html"
    success_url = reverse_lazy("administracion:listar_profesion")
    def form_valid(self, form):
        nombre_profesion = form.cleaned_data['nombre_profesion']
        if Profesion.objects.filter(nombre_profesion=nombre_profesion).exists():
            form.add_error('nombre_profesion', 'Profesion with this name already exists.')
            return self.form_invalid(form)
        return super().form_valid(form)


class ListadoProfesion(ListView):
    model = Profesion
    template_name = "administracion/gui_profesion/listar_profesion.html"
    context_object_name = "profesiones"
    queryset = Profesion.objects.all()


class ActualizarProfesion(UpdateView):
    model = Profesion
    form_class = ProfesionForm
    template_name = "administracion/gui_profesion/crear_profesion.html"
    success_url = reverse_lazy("administracion:listar_profesion")
