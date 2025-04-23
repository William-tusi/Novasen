from django.db import models
from .regional_models import Regional

class Sedes(models.Model):
    codigo = models.CharField(max_length=50, null=False, unique=True)
    nombre = models.CharField(max_length=255, null=False)
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre
