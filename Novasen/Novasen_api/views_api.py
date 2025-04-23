from rest_framework import viewsets
from .models import Rol, Usuario, Provincia, Ciudad, Sedes, Ambiente, Fichas, Programas, Regional
from .serializers import RolSerializer, UsuarioSerializer, ProvivenciaSerializer, CiudadSerializer, SedesSerializer, AmbienteSerializer, FichasSerializer, ProgramasSerializer, RegionalSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProvivenciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvivenciaSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class SedesViewSet(viewsets.ModelViewSet):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class FichasViewSet(viewsets.ModelViewSet):
    queryset = Fichas.objects.all()
    serializer_class = FichasSerializer

class ProgramasViewSet(viewsets.ModelViewSet):
    queryset = Programas.objects.all()
    serializer_class = ProgramasSerializer

class RegionalViewSet(viewsets.ModelViewSet):
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer
