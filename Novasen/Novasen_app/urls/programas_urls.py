from django.urls import path
from Novasen_app.views.programas_views import insertar_programas, listar_programas

urlpatterns = [
    path('insertar/', insertar_programas, name='insertar_programas'),
    path('listar/', listar_programas, name='listar_programas'),
]
