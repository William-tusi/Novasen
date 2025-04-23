from django.urls import path
from Novasen_app.views.usuario_views import *


urlpatterns = [
    # Rutas para usuarios
    path('insertar/', insertar_usuario, name='insertar_usu'),
    path('listar/', listar_usu, name='listar_usu'),
    path('actualizar/<int:id>/', actualizar_usu, name='actualizar_usu'),
    path('eliminar/<int:id>/', eliminar_usu, name='eliminar_usu'),
    # Ruta para login
    path('login/', login, name='login'),
    
    

]
