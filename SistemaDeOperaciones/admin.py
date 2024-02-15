# tu_proyecto/admin.py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render

class CustomAdminSite(admin.AdminSite):
    site_header = 'Tu Título Personalizado'
    site_title = 'Tu Título Personalizado'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('pagina1/', self.admin_view(self.pagina1_view), name='pagina1'),
            path('pagina2/', self.admin_view(self.pagina2_view), name='pagina2'),
        ]
        return custom_urls + urls

    def pagina1_view(self, request):
        # Lógica personalizada si es necesario antes de renderizar la página
        return render(request, 'tu_template_pagina1.html')

    def pagina2_view(self, request):
        # Lógica personalizada si es necesario antes de renderizar la página
        return render(request, 'tu_template_pagina2.html')

admin_site = CustomAdminSite(name='admin')

# admin_site.register(TuModelo)  # Asegúrate de registrar tus modelos aquí

