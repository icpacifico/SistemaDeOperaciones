from django.contrib import admin
from .models import *
# Register your models here.


class ViviendaAdmin(admin.ModelAdmin):
    search_fields = ['nombre_vivienda']


admin.site.register(Condominio)
admin.site.register(Etapa)
admin.site.register(Torre)
admin.site.register(Modelo)
admin.site.register(Bodega)
admin.site.register(Estacionamiento)
admin.site.register(Vivienda, ViviendaAdmin)
