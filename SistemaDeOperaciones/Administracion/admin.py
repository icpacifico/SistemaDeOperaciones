from django.contrib import admin
from .models import Nacionalidad, Banco, ConjuntoParametros, Profesion

# Registro de los modelos en el panel de administración

@admin.register(Nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('id_nacionalidad', 'nombre_nacionalidad')
    search_fields = ('nombre_nacionalidad',)

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('id_banco', 'nombre_banco')
    search_fields = ('nombre_banco',)

@admin.register(ConjuntoParametros)
class ConjuntoParametrosAdmin(admin.ModelAdmin):
    list_display = ('id_conjunto_parametros', 'id_condominio', 'factor_vendedor', 'precio_dcto_depto')
    list_filter = ('id_condominio',)
    search_fields = ('id_condominio__nombre_condominio',)

@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('id_profesion', 'nombre_profesion')
    search_fields = ('nombre_profesion',)
