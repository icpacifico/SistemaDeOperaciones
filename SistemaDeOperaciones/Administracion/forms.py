from django import forms
from .models import Nacionalidad, Banco, ConjuntoParametros, Profesion
from django.contrib.auth.forms import AuthenticationForm

 
class FormularioLogin(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(FormularioLogin, self)._init_(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'



# Formulario para Nacionalidad
class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = ['nombre_nacionalidad']
        labels = {'nombre_nacionalidad': 'Nacionalidad'}
        widgets = {
            'nombre_nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': ''}),
        }

# Formulario para Banco
class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nombre_banco']
        labels = {'nombre_banco': 'Banco'}
        widgets = {
            'nombre_banco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': ''}),
        }

# Formulario para ConjuntoParametros
class ConjuntoParametrosForm(forms.ModelForm):
    class Meta:
        model = ConjuntoParametros
        fields = [
            'id_condominio', 'factor_vendedor', 'precio_dcto_depto', 'bono_precio_porce',
            'porcen_promesa', 'porcen_escritura', 'porcen_comision_vendedor', 'monto_escrt_operaciones',
            'monto_reserva', 'monto_prorrateo', 'monto_recuperar', 'fecha_recuperacion', 'valor_bodega',
            'valor_estacionamiento', 'fecha_termino_venta', 'direccion_condominio', 'banco_alzante'
        ]
        labels = {
            'id_condominio': 'Condominio',
            'factor_vendedor': 'Factor',
            'precio_dcto_depto': 'Precio descuento Depto',
            'bono_precio_porce': 'Porcentaje Bono Precio',
            'porcen_promesa': 'Porcentaje Promesa',
            'porcen_escritura': 'Porcentaje Escritura',
            'porcen_comision_vendedor': '% comisión Vendedor',
            'monto_escrt_operaciones': 'Monto Escritura Operaciones (UF)',
            'monto_reserva': 'Monto Reserva (UF)',
            'monto_prorrateo': 'Monto a Prorratear',
            'monto_recuperar': 'Monto a Recuperar',
            'fecha_recuperacion': 'Fecha Recuperación',
            'valor_bodega': '$ Bodega',
            'valor_estacionamiento': '$ Estacionamiento',
            'fecha_termino_venta': 'Fecha termino de ventas',
            'direccion_condominio': 'Dirección Condominio',
            'banco_alzante': 'Banco Alzante',
        }
        widgets = {
            'id_condominio': forms.Select(attrs={'class': 'form-control'}),
            'factor_vendedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_dcto_depto': forms.NumberInput(attrs={'class': 'form-control'}),
            'bono_precio_porce': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcen_promesa': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcen_escritura': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcen_comision_vendedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_escrt_operaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_reserva': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_prorrateo': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_recuperar': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_recuperacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor_bodega': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_estacionamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_termino_venta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion_condominio': forms.TextInput(attrs={'class': 'form-control'}),
            'banco_alzante': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulario para Profesion
class ProfesionForm(forms.ModelForm):
    class Meta:
        model = Profesion
        fields = ['nombre_profesion']
        labels = {'nombre_profesion': 'Profesión'}
        widgets = {
            'nombre_profesion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'id': ''}),
        }
