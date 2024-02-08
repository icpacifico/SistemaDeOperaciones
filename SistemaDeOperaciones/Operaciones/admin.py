from django.contrib import admin
from .models import *
from Ventas.models import Venta

# Register your models here.


admin.site.register(CategoriaEtapa)
admin.site.register(Etapa)
admin.site.register(CampoEtapa)
admin.site.register(Operacione)

# Registra el modelo Venta directamente
# admin.site.register(Venta)
