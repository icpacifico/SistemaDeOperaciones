from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Nacionalidad, Banco, ConjuntoParametros, Profesion
# Create your views here.



"""
# Vistas basadas en clases de Banco
class CrearBanco(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'gui_administracion/gui_banco/crear_banco.html'
    success_url = reverse_lazy('administracion:listar_banco')


class ListadoBanco(ListView):
    model = Banco
    template_name = 'gui_administracion/gui_banco/listar_banco.html'
    context_object_name = 'bancos'
    queryset = Banco.objects.all()


class ActualizarBanco(UpdateView):
    model = Banco
    template_name = 'gui_administracion/gui_banco/crear_banco.html'
    form_class = BancoForm
    success_url =  reverse_lazy('administracion:listar_banco')"""