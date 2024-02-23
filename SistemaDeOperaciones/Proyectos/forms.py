from django import forms
from .models import Condominio, Etapa, Torre, Modelo, Bodega, Estacionamiento, Vivienda

class CondominioForm(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = ['estado_condominio', 'nombre_condominio', 'fecha_venta_condominio']
        labels = {
            'estado_condominio': 'Estado',
            'nombre_condominio': 'Nombre',
            'fecha_venta_condominio': 'Fecha Venta Condominio',
        }
        widgets = {
            'estado_condominio': forms.Select(attrs={'class': 'form-select'}),
            'nombre_condominio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_venta_condominio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['id_condominio', 'nombre_etapa']
        labels = {
            'id_condominio': 'Condominio',
            'nombre_etapa': 'Nombre',
        }
        widgets = {
            'id_condominio': forms.Select(attrs={'class': 'form-select'}),
            'nombre_etapa': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TorreForm(forms.ModelForm):
    class Meta:
        model = Torre
        fields = ['id_etapa_condominio', 'estado_torre', 'nombre_torre']
        labels = {
            'id_etapa_condominio': 'Etapa',
            'estado_torre': 'Estado',
            'nombre_torre': 'Nombre',
        }
        widgets = {
            'id_etapa_condominio': forms.Select(attrs={'class': 'form-select'}),
            'estado_torre': forms.Select(attrs={'class': 'form-select'}),
            'nombre_torre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['estado_modelo', 'nombre_modelo', 'numero_cama_modelo', 'numero_bagno_modelo', 'descripcion_modelo']
        labels = {
            'estado_modelo': 'Estado',
            'nombre_modelo': 'Nombre',
            'numero_cama_modelo': 'N° camas',
            'numero_bagno_modelo': 'N° baños',
            'descripcion_modelo': 'Descripción',
        }
        widgets = {
            'estado_modelo': forms.Select(attrs={'class': 'form-select'}),
            'nombre_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_cama_modelo': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_bagno_modelo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion_modelo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['estado_bodega', 'nombre_bodega', 'valor_bodega', 'rol_bodega']
        labels = {
            'estado_bodega': 'Estado',
            'nombre_bodega': 'Nombre',
            'valor_bodega': 'Valor',
            'rol_bodega': 'Rol',
        }
        widgets = {
            'estado_bodega': forms.Select(attrs={'class': 'form-select'}),
            'nombre_bodega': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_bodega': forms.NumberInput(attrs={'class': 'form-control'}),
            'rol_bodega': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ['id_etapa', 'estado_estacionamiento', 'nombre_estacionamiento', 'valor_estacionamiento']
        labels = {
            'id_etapa': 'Etapa',
            'estado_estacionamiento': 'Estado',
            'nombre_estacionamiento': 'Nombre',
            'valor_estacionamiento': 'Valor',
        }
        widgets = {
            'id_etapa': forms.Select(attrs={'class': 'form-select'}),
            'estado_estacionamiento': forms.Select(attrs={'class': 'form-select'}),
            'nombre_estacionamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_estacionamiento': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = ['id_torre', 'id_modelo', 'tipo_vivienda', 'ori_vivienda', 'estado_vivienda', 'piso',
                  'nombre_vivienda', 'valor_vivienda', 'metros_vivienda', 'metros_terraza_vivienda',
                  'metros_total_vivienda', 'bono_vivienda', 'prorrateo_vivienda', 'rol_vivienda']
        labels = {
            'id_torre': 'Torre',
            'id_modelo': 'Modelo',
            'tipo_vivienda': 'Tipo',
            'ori_vivienda': 'Orientación',
            'estado_vivienda': 'Estado vivienda',
            'piso': 'Piso',
            'nombre_vivienda': 'Número',
            'valor_vivienda': 'Valor',
            'metros_vivienda': 'Metros depto',
            'metros_terraza_vivienda': 'Metros terraza',
            'metros_total_vivienda': 'Metros total',
            'bono_vivienda': '% Descuento',
            'prorrateo_vivienda': '% Prorrateo',
            'rol_vivienda': 'Rol',
        }
        widgets = {
            'id_torre': forms.Select(attrs={'class': 'form-select'}),
            'id_modelo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_vivienda': forms.Select(attrs={'class': 'form-select'}),
            'ori_vivienda': forms.Select(attrs={'class': 'form-select'}),
            'estado_vivienda': forms.Select(attrs={'class': 'form-select'}),
            'piso': forms.Select(attrs={'class': 'form-select'}),
            'nombre_vivienda': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'metros_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'metros_terraza_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'metros_total_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'bono_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'prorrateo_vivienda': forms.NumberInput(attrs={'class': 'form-control'}),
            'rol_vivienda': forms.TextInput(attrs={'class': 'form-control'}),
        }
