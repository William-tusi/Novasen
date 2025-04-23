from django.contrib import admin
from django.contrib import admin
from .models import Rol, Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Rol)
admin.site.register(Usuario, UserAdmin)

# Register your models here.
