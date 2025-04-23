from rest_framework.routers import DefaultRouter
from Novasen_api.views import RolViewSet, UsuarioViewSet, ProvivenciaViewSet, CiudadViewSet, SedesViewSet, AmbienteViewSet, FichasViewSet, ProgramasViewSet, RegionalViewSet

router = DefaultRouter()
router.register(r'rol', RolViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'provivencia', ProvivenciaViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'sedes', SedesViewSet)
router.register(r'ambiente', AmbienteViewSet)
router.register(r'fichas', FichasViewSet)
router.register(r'programas', ProgramasViewSet)
router.register(r'regional', RegionalViewSet)

urlpatterns = router.urls
