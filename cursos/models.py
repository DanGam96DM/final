from django.db import models
from django.utils import timezone


class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
