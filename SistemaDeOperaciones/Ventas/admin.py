from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Profesion)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(TipoDesistimiento) # Quizás sea necesario moverlo al panel de admin
admin.site.register(Desistimiento)