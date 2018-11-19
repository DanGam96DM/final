from django.contrib import admin
from .models import Profesores, ProfesoresAdmin, Curso, CursoAdmin

admin.site.register(Profesores, ProfesoresAdmin)
admin.site.register(Curso, CursoAdmin)
