from django.db import models

class Provivencia(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True)
    provivencia = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.provivencia
