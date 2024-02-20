from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView, FormView
from .models import Nacionalidad, Banco, ConjuntoParametros, Profesion
from . forms import *
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class Inicio(TemplateView):
    template_name = 'pages/index.html'
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
    template_name = "administracion/gui_conjunto_parametros/crear_conjunto_parametros.html"
    success_url = reverse_lazy("administracion:listar_conjunto_parametros")


class ListadoConjuntoParametros(ListView):
    model = ConjuntoParametros
    template_name = "administracion/gui_conjunto_parametros/listar_conjunto_parametros.html"
    context_object_name = "conjunto_parametros"
    queryset = ConjuntoParametros.objects.all()


class ActualizarConjuntoParametros(UpdateView):
    model = ConjuntoParametros
    form_class = ConjuntoParametrosForm
    template_name = "administracion/gui_conjunto_parametros/crear_conjunto_parametros.html"
    success_url = reverse_lazy("administracion:listar_conjunto_parametros")



# Vistas basadas en clases de Profesion
class CrearProfesion(CreateView):
    model = Profesion
    form_class = ProfesionForm
    template_name = "administracion/gui_profesion/crear_profesion.html"
    success_url = reverse_lazy("administracion:listar_profesion")


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
