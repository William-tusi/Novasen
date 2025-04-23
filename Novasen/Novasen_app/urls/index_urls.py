# Novasen_app urls

from django.urls import path ,include
from Novasen_app.views import perfil, registrar ,index  ,insertar_usuario        # Importa las vistas desde la carpeta 'views'

urlpatterns = [
 
    path('', index, name="index"),
    path('registro/', registrar, name="registro"),
    path('usuario/perfil/', perfil, name="perfil_usuario"),
    path('registro/', insertar_usuario, name='insetar_usuario'),
    
]
