# En myapp/views.py

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def custom_admin_view(request):
    # Lógica de tu vista personalizada aquí
    context = {
        'custom_data': 'Hola desde la vista personalizada',
    }
    return render(request, 'admin/Operaciones/custom_admin_view.html', context)