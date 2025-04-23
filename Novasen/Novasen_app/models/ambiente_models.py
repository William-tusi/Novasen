from django.db import models
from .sedes_models import Sedes

class Ambiente(models.Model):
    piso = models.CharField(max_length=50, null=False)
    ambiente = models.CharField(max_length=255, null=False)
    sede = models.ForeignKey(Sedes, on_delete=models.PROTECT)

    def __str__(self):
        return self.ambiente
