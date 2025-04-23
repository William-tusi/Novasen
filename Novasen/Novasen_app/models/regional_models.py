from django.db import models

class Regional(models.Model):
    nit = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=255, null=False)
    ciudad = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nombre
