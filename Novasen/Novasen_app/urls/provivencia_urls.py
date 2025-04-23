from django.urls import path
from Novasen_app.views.provivencia_views import insertar_provivencia, listar_provivencia, actualizar_provivencia, eliminar_provivencia

urlpatterns = [
    path('insertar/', insertar_provivencia, name='insertar_provievncia'),
    path('listar/', listar_provivencia, name='listar_provivencia'),
    path('actualizar/<int:id>/', actualizar_provivencia, name='actualizar_provivencia'),
    path('eliminar/<int:id>/', eliminar_provivencia, name='eliminar_provivencia'),
]
