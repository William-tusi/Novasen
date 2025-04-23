from django.db import models
from .provivencia_models import Provivencia

class Ciudad(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True)
    ciudad = models.CharField(max_length=100, null=False)
    provivencia = models.ForeignKey(Provivencia, on_delete=models.PROTECT, default=1)
    def __str__(self):
        return self.ciudad
