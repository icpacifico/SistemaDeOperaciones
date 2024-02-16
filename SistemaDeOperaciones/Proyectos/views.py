from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Condominio, Etapa, Torre, Modelo, Bodega, Estacionamiento, Vivienda
from .forms import CondominioForm, EtapaForm, TorreForm, ModeloForm, BodegaForm, EstacionamientoForm, ViviendaForm
# Create your views here.


class CrearCondominio(CreateView):
    model = Condominio
    form_class = CondominioForm
    template_name = "proyectos/gui_condominio/crear_condominio.html"
    success_url = reverse_lazy("proyectos:listar_condominio")

class ListadoCondominio(ListView):
    model = Condominio
    template_name = "proyectos/gui_condominio/listar_condominio.html"
    context_object_name = "condominios"
    queryset = Condominio.objects.all()

class ActualizarCondominio(UpdateView):
    model = Condominio
    template_name = "proyectos/gui_condominio/editar_condominio.html"
    form_class = CondominioForm
    success_url = reverse_lazy("proyectos:listar_condominio")

class CrearEtapa(CreateView):
    model = Etapa
    form_class = EtapaForm
    template_name = "proyectos/gui_etapa/crear_etapa.html"
    success_url = reverse_lazy("proyectos:listar_etapa")

class ListadoEtapa(ListView):
    model = Etapa
    template_name = "proyectos/gui_etapa/listar_etapa.html"
    context_object_name = "etapas"
    queryset = Etapa.objects.all()

class ActualizarEtapa(UpdateView):
    model = Etapa
    template_name = "proyectos/gui_etapa/editar_etapa.html"
    form_class = EtapaForm
    success_url = reverse_lazy("proyectos:listar_etapa")

class CrearTorre(CreateView):
    model = Torre
    form_class = TorreForm
    template_name = "proyectos/gui_torre/crear_torre.html"
    success_url = reverse_lazy("proyectos:listar_torre")

class ListadoTorre(ListView):
    model = Torre
    template_name = "proyectos/gui_torre/listar_torre.html"
    context_object_name = "torres"
    queryset = Torre.objects.all()

class ActualizarTorre(UpdateView):
    model = Torre
    template_name = "proyectos/gui_torre/editar_torre.html"
    form_class = TorreForm
    success_url = reverse_lazy("proyectos:listar_torre")

class CrearModelo(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = "proyectos/gui_modelo/crear_modelo.html"
    success_url = reverse_lazy("proyectos:listar_modelo")

class ListadoModelo(ListView):
    model = Modelo
    template_name = "proyectos/gui_modelo/listar_modelo.html"
    context_object_name = "modelos"
    queryset = Modelo.objects.all()

class ActualizarModelo(UpdateView):
    model = Modelo
    template_name = "proyectos/gui_modelo/editar_modelo.html"
    form_class = ModeloForm
    success_url = reverse_lazy("proyectos:listar_modelo")

class CrearBodega(CreateView):
    model = Bodega
    form_class = BodegaForm
    template_name = "proyectos/gui_bodega/crear_bodega.html"
    success_url = reverse_lazy("proyectos:listar_bodega")

class ListadoBodega(ListView):
    model = Bodega
    template_name = "proyectos/gui_bodega/listar_bodega.html"
    context_object_name = "bodegas"
    queryset = Bodega.objects.all()

class ActualizarBodega(UpdateView):
    model = Bodega
    template_name = "proyectos/gui_bodega/editar_bodega.html"
    form_class = BodegaForm
    success_url = reverse_lazy("proyectos:listar_bodega")

class CrearEstacionamiento(CreateView):
    model = Estacionamiento
    form_class = EstacionamientoForm
    template_name = "proyectos/gui_estacionamiento/crear_estacionamiento.html"
    success_url = reverse_lazy("proyectos:listar_estacionamiento")

class ListadoEstacionamiento(ListView):
    model = Estacionamiento
    template_name = "proyectos/gui_estacionamiento/listar_estacionamiento.html"
    context_object_name = "estacionamientos"
    queryset = Estacionamiento.objects.all()

class ActualizarEstacionamiento(UpdateView):
    model = Estacionamiento
    template_name = "proyectos/gui_estacionamiento/editar_estacionamiento.html"
    form_class = EstacionamientoForm
    success_url = reverse_lazy("proyectos:listar_estacionamiento")

class CrearVivienda(CreateView):
    model = Vivienda
    form_class = ViviendaForm
    template_name = "proyectos/gui_vivienda/crear_vivienda.html"
    success_url = reverse_lazy("proyectos:listar_vivienda")

class ListadoVivienda(ListView):
    model = Vivienda
    template_name = "proyectos/gui_vivienda/listar_vivienda.html"
    context_object_name = "viviendas"
    queryset = Vivienda.objects.all()

class ActualizarVivienda(UpdateView):
    model = Vivienda
    template_name = "proyectos/gui_vivienda/editar_vivienda.html"
    form_class = ViviendaForm
    success_url = reverse_lazy("proyectos:listar_vivienda")