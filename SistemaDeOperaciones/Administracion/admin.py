from django.contrib import admin
from .models import *
# Register your models here.

# Registro de modelos en el panel Admin
admin.site.register(Banco)
admin.site.register(ConjuntoParametros)
admin.site.register(Nacionalidad)
admin.site.register(Profile)