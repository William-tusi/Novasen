from django.db import models

class Rol(models.Model):
    codigo = models.CharField(max_length=100, unique=False, default='default_value')
    nombre = models.CharField(max_length=50, unique=True, default='Aprendiz')
    descripcion = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nombre
