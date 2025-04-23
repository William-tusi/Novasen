from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    codigo = models.CharField(max_length=100, unique=False, default='default_value')
    nombre = models.CharField(max_length=50, unique=True, default='Aprendiz')
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):
    TIPO_DOC = [
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('OT', 'Otro')
    ]
    tipo_doc = models.CharField(max_length=2, choices=TIPO_DOC, default='CC')
    num_doc = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username


class Provincia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.provincia


class Ciudad(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    ciudad = models.CharField(max_length=100)
    provincia = models.ForeignKey('Provincia', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.ciudad


class Regional(models.Model):
    nit = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Sedes(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    regional = models.ForeignKey('Regional', on_delete=models.PROTECT)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ambiente(models.Model):
    piso = models.CharField(max_length=50)
    ambiente = models.CharField(max_length=255)
    sede = models.ForeignKey('Sedes', on_delete=models.PROTECT)

    def __str__(self):
        return self.ambiente


class Fichas(models.Model):
    ficha = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    ambiente = models.ForeignKey('Ambiente', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Programas(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)
    horas = models.CharField(max_length=255)
    version = models.CharField(max_length=100)
    ficha = models.ForeignKey('Fichas', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
