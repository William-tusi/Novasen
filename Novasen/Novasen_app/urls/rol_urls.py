from django.urls import path
from Novasen_app.views.rol_views import insertar_rol, listar_rol, actualizar_rol, eliminar_rol

urlpatterns = [
    path('insertar/', insertar_rol, name='insertar_rol'),
    path('listar/', listar_rol, name='listar_rol'),
    path('actualizar/<int:id>/', actualizar_rol, name='actualizar_rol'),
    path('eliminar/<int:id>/', eliminar_rol, name='eliminar_rol'),
]
