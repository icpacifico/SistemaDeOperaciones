from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['forma_pago', 'id_venta', 'id_banco', 'categoria_pago', 'estado_pago', 'numero_documento', 'numero_serie', 'fecha_pago', 'fecha_real_pago', 'monto_pago', 'descripcion']
        labels = {
            'forma_pago': 'Forma de Pago',
            'id_venta': 'Venta',
            'id_banco': 'Banco',
            'categoria_pago': 'Categoría de Pago',
            'estado_pago': 'Estado de Pago',
            'numero_documento': 'N° de Documento',
            'numero_serie': 'N° de Serie',
            'fecha_pago': 'Fecha de Pago',
            'fecha_real_pago': 'Fecha Real de Pago',
            'monto_pago': 'Monto de Pago',
            'descripcion': 'Descripción',
        }
        widgets = {
            'forma_pago': forms.Select(attrs={'class': 'form-select'}),
            'id_venta': forms.Select(attrs={'class': 'form-select'}),
            'id_banco': forms.Select(attrs={'class': 'form-select'}),
            'categoria_pago': forms.Select(attrs={'class': 'form-select'}),
            'estado_pago': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_serie': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_real_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto_pago': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
