from django.shortcuts import render
from .forms import AsignacionForm
from .models import Profesores, Asignacion, Curso

from django.contrib import messages
def profesor_list(request):
    profesores = Profesores.objects.order_by('fecha_nacimiento')
    return render(request, 'curso/profesor_list.html', {'profesores':profesores})
def profesor_nuevo(request):
    if request.method == "POST":
        formulario = AsignacionForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'])
            for profesor_id in request.POST.getlist('profesores'):
                asignacion = Asignacion(profesor_id=profesor_id, curso_id = curso.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Asignacion Guardada Exitosamente')
    else:
        formulario = AsignacionForm()
    return render(request, 'curso/profesor_editar.html', {'formulario': formulario})
