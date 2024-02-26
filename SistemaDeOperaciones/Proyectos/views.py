from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from openpyxl import Workbook
from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView, DetailView
)
import pandas as pd
from .models import (
    Condominio, Etapa, Torre, Modelo, Bodega, Estacionamiento, Vivienda
)
from .forms import (
    CondominioForm, EtapaForm, TorreForm, ModeloForm,
    BodegaForm, EstacionamientoForm, ViviendaForm, ImportViviendasForm
)
from SistemaDeOperaciones.choices import *


# Create your views here.

def descargar_parametros(request):
    # Crea un nuevo libro de Excel
    wb = Workbook()

    # Define modelos y sus nombres para hojas
    modelos = [
        (Torre, 'Torre'),
        (Modelo, 'Modelo'),
        (Bodega, 'Bodega'),
        (Estacionamiento, 'Estacionamiento'),
    ]

    # Para cada modelo, agrega una hoja al libro y llena los datos
    for modelo, nombre_hoja in modelos:
        hoja = wb.create_sheet(title=nombre_hoja)
        # Agrega dinámicamente encabezados de columnas desde el modelo
        headers = [field.name for field in modelo._meta.fields]
        hoja.append(headers)
        # Agrega datos del modelo
        objetos_modelo = modelo.objects.all()
        for obj in objetos_modelo:
            row_data = [getattr(obj, field.name) for field in modelo._meta.fields]
            hoja.append(row_data)

    # Configura la respuesta HTTP para devolver un archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=parametros.xlsx'

    # Guarda el libro de Excel en la respuesta
    wb.save(response)

    return response
def descargar_formato(request):
    # Crea un DataFrame con las columnas que deseas en el formato del archivo Excel
    columns = [
        'id_torre', 'id_modelo', 'tipo_vivienda', 'ori_vivienda', 'estado_vivienda', 'piso',
        'nombre_vivienda', 'valor_vivienda', 'metros_vivienda', 'metros_terraza_vivienda', 'metros_total_vivienda',
        'bono_vivienda', 'prorrateo_vivienda', 'rol_vivienda'
    ]
    df = pd.DataFrame(columns=columns)
    # Crea una respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=formato_carga.xlsx'
    # Guarda el DataFrame en el archivo Excel
    df.to_excel(response, index=False, engine='openpyxl')
    return response


def importar_viviendas(request):
    if request.method == 'POST':
        form = ImportViviendasForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = request.FILES['archivo_excel']
            try:
                # Leer el archivo Excel usando pandas
                df = pd.read_excel(archivo_excel, engine='openpyxl')

                # Iterar sobre las filas del DataFrame y crear instancias de Vivienda
                viviendas = []
                for index, row in df.iterrows():
                    Vivienda.objects.create(
                        id_torre=row['id_torre'],
                        id_modelo=row['id_modelo'],
                        tipo_vivienda=row['tipo_vivienda'],
                        ori_vivienda=row['ori_vivienda'],
                        estado_vivienda=row['estado_vivienda'],
                        piso=row['piso'],
                        nombre_vivienda=row['nombre_vivienda'],
                        valor_vivienda=row['valor_vivienda'],
                        metros_vivienda=row['metros_vivienda'],
                        metros_terraza_vivienda=row['metros_terraza_vivienda'],
                        metros_total_vivienda=row['metros_total_vivienda'],
                        bono_vivienda=row['bono_vivienda'],
                        prorrateo_vivienda=row['prorrateo_vivienda'],
                        rol_vivienda=row['rol_vivienda']
                    )

                # Mensaje de éxito
                success_message = f"Importación de datos exitosa. Se han cargado {len(viviendas)} registros."

                # Redirigir al usuario con un mensaje de éxito
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success_message': success_message})
                else:
                    return redirect('./listar_vivienda')
            except Exception as e:
                # Manejar cualquier error durante la importación
                error_message = f"Error durante la importación: {str(e)}"
                return render(request, 'proyectos/gui_condominio/importar_viviendas.html', {'form': form, 'error_message': error_message})
    else:
        form = ImportViviendasForm()

    return render(request, 'proyectos/gui_condominio/importar_viviendas.html', {'form': form})




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
    template_name = "proyectos/gui_condominio/crear_condominio.html"
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
    template_name = "proyectos/gui_etapa/crear_etapa.html"
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
    template_name = "proyectos/gui_torre/crear_torre.html"
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
    template_name = "proyectos/gui_modelo/crear_modelo.html"
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
    template_name = "proyectos/gui_bodega/crear_bodega.html"
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
    template_name = "proyectos/gui_estacionamiento/crear_estacionamiento.html"
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
    template_name = "proyectos/gui_vivienda/crear_vivienda.html"
    form_class = ViviendaForm
    success_url = reverse_lazy("proyectos:listar_vivienda")
