from django.db import models
from django.contrib.auth.models import AbstractUser
from .rol_models import Rol

class Usuario(AbstractUser):
    TIPO_DOC = [
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cedula de ciudania'),
        ('CE', 'Cedula de extranjeria'),
        ('OT', 'Otro')
    ]
    
    tipo_doc = models.CharField(max_length=2, choices=TIPO_DOC, default='CC')
    num_doc = models.CharField(max_length=20, null=False)
    telefono = models.CharField(max_length=30, blank=False, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    # Adding related_name to avoid clashes with reverse accessors
    groups = models.ManyToManyField('auth.Group', related_name='novasen_app_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='novasen_app_permissions', blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
