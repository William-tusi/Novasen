from django.contrib import admin
from .models import Rol, Usuario, Provivencia, Ciudad, Regional, Sedes, Ambiente, Fichas, Programas

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('piso', 'ambiente', 'get_sede_name')
    search_fields = ('ambiente', 'piso')
    list_filter = ('sede',)  # ← Asegúrate que el campo se llama 'sede'

    def get_sede_name(self, obj):
        return obj.sede.nombre  # ← Corregido de 'sedes' a 'sede'
    get_sede_name.admin_order_field = 'sede'
    get_sede_name.short_description = 'Sede'

@admin.register(Programas)
class ProgramasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'horas', 'version')  # Eliminado 'get_fichas_code'
    search_fields = ('codigo', 'nombre', 'horas', 'version')
    # list_filter eliminado si no existe relación directa con fichas

@admin.register(Fichas)
class FichasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_ficha', 'ambiente')  # ← Usa el campo correcto en vez de 'codigo'
    search_fields = ('nombre',)
    list_filter = ('ambiente',)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion')
    search_fields = ('nombre', 'codigo')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'tipo_doc', 'num_doc', 'telefono', 'rol')
    search_fields = ('username', 'num_doc', 'tipo_doc')
    list_filter = ('rol',)

@admin.register(Provivencia)
class ProvivenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'provivencia')
    search_fields = ('provivencia', 'codigo')

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'ciudad', 'provivencia')
    search_fields = ('ciudad', 'codigo')
    list_filter = ('provivencia',)

@admin.register(Regional)
class RegionalAdmin(admin.ModelAdmin):
    list_display = ('nit', 'nombre', 'ciudad')
    search_fields = ('nombre', 'nit', 'ciudad')

@admin.register(Sedes)
class SedesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'regional', 'direccion')
    search_fields = ('nombre', 'codigo')
    list_filter = ('regional',)
