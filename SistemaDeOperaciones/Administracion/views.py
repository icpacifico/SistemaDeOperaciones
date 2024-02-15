from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Nacionalidad, Banco, ConjuntoParametros, Profesion
# Create your views here.



# Vistas basadas en clases de Nacionalidad
class CrearNacionalidad(CreateView):
    model = Nacionalidad
    form_class = ""
    template_name = ""
    success_url = ""


class ListadoNacionalidad(ListView):
    model = Nacionalidad
    template_name = ""
    context_object_name = ""
    queryset = ""


class ActualizarNacionalidad(UpdateView):
    model = Nacionalidad
    template_name = ""
    form_class = ""
    success_url =  ""


# Vistas basadas en clases de Banco
class CrearBanco(CreateView):
    model = Banco
    form_class = ""
    template_name = ""
    success_url = ""


class ListadoBanco(ListView):
    model = Banco
    template_name = ""
    context_object_name = ""
    queryset = ""


class ActualizarBanco(UpdateView):
    model = Banco
    template_name = ""
    form_class = ""
    success_url =  ""


# Vistas basadas en clases de ConjuntoParametros
class CrearConjuntoParametros(CreateView):
    model = ConjuntoParametros
    form_class = ""
    template_name = ""
    success_url = ""


class ListadoConjuntoParametros(ListView):
    model = ConjuntoParametros
    template_name = ""
    context_object_name = ""
    queryset = ""


class ActualizarConjuntoParametros(UpdateView):
    model = ConjuntoParametros
    template_name = ""
    form_class = ""
    success_url =  ""


# Vistas basadas en clases de Profesion
class CrearProfesion(CreateView):
    model = Profesion
    form_class = ""
    template_name = ""
    success_url = ""


class ListadoProfesion(ListView):
    model = Profesion
    template_name = ""
    context_object_name = ""
    queryset = ""


class ActualizarProfesion(UpdateView):
    model = Profesion
    template_name = ""
    form_class = ""
    success_url =  ""