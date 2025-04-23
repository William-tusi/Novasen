from rest_framework import serializers
from .models import Rol, Usuario, Provivencia, Ciudad, Sedes, Ambiente, Fichas, Programas, Regional

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'codigo', 'descripcion']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'tipo_doc', 'num_doc', 'first_name', 'last_name', 'username', 'email', 'telefono', 'rol']

class ProvivenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provivencia
        fields = ['id', 'codigo', 'provincia']

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', 'codigo', 'ciudad', 'provincia']

class SedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = ['id', 'codigo', 'nombre', 'direccion', 'regional']

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['id', 'piso', 'salon']

class FichasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichas
        fields = ['id', 'ficha', 'nombre', 'ambiente']

class ProgramasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programas
        fields = ['id', 'codigo', 'nombre', 'horas', 'version', 'ficha']

class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = ['id', 'nit', 'nombre', 'ciudad']
