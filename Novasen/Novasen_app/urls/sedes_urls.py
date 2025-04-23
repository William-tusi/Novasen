from django.urls import path
from Novasen_app.views.sedes_views import insertar_sedes, listar_sedes, actualizar_sedes, eliminar_sedes

urlpatterns = [
    path('insertar/', insertar_sedes, name='insertar_sedes'),
    path('listar/', listar_sedes, name='listar_sedes'),
    path('actualizar/<int:id>/', actualizar_sedes, name='actualizar_sedes'),
    path('eliminar/<int:id>/', eliminar_sedes, name='eliminar_sedes'),
]
