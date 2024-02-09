# En Operaciones/urls.py

from django.urls import path
from .views import custom_admin_view

urlpatterns = [
    path('', custom_admin_view, name='operaciones_home'),  # Puedes cambiar el nombre según tus preferencias
    path('custom_admin_view/', custom_admin_view, name='custom_admin_view'),
    # Otras URL de tu aplicación
]
