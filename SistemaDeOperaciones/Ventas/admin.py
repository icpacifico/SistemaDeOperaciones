from django.contrib import admin
from .models import *
from Operaciones.models import Operacione
# Register your models here.

class OperacionesInline(admin.TabularInline):
    model = Operacione

# Añade la clase ModelAdmin si es necesario
class VentaAdmin(admin.ModelAdmin):
    inlines = [OperacionesInline,]

admin.site.register(Profesion)
admin.site.register(Cliente)

admin.site.register(Venta, VentaAdmin)

admin.site.register(TipoDesistimiento) # Quizás sea necesario moverlo al panel de admin
admin.site.register(Desistimiento)
