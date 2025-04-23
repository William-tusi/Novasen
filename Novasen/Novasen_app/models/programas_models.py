from django.db import models
from .fichas_models import Fichas

class Programas(models.Model):
    codigo = models.CharField(max_length=50, null=False, unique=True)
    nombre = models.CharField(max_length=255, null=False)
    horas = models.CharField(max_length=255, null=False)
    version = models.CharField(max_length=100, null=False)
    ficha = models.ForeignKey(Fichas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
