from django.db import models
from django.contrib import admin
from django.utils import timezone


class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=10)
    profesores   = models.ManyToManyField(Profesores, through='Asignacion')
    def __str__(self):
        return self.nombre
class Asignacion(models.Model):
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class ProfesoresAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
