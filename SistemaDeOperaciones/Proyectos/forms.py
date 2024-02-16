from django import forms
from .models import Condominio, Etapa, Torre, Modelo, Bodega, Estacionamiento, Vivienda
 
# Formulario para Condominio
class CondominioForm(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = '__all__'

# Formulario para Etapa
class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = '__all__'

# Formulario para Torre
class TorreForm(forms.ModelForm):
    class Meta:
        model = Torre
        fields = '__all__'

# Formulario para Modelo
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

# Formulario para Bodega
class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

# Formulario para Estacionamiento
class EstacionamientoForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = '__all__'

# Formulario para Vivienda
class ViviendaForm(forms.ModelForm):
    class Meta:
        model = Vivienda
        fields = '__all__'