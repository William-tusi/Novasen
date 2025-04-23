from django.db import models
from .ambiente_models import Ambiente


class Fichas(models.Model):
    nombre = models.CharField(max_length=100)
    numero_ficha = models.CharField(max_length=50)  # Asegúrate de que este campo existe
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

