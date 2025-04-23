# Novasen_app/urls/user_urls.py
from django.urls import path
from Novasen_app.views import *

urlpatterns = [
    path('insertar/', insertar_usuario, name="insertar_usuario"),
    path('listar/', listar_usu, name='listar_usu'),
    path('eliminar/<int:id>/', eliminar_usu, name='eliminar_usu'),
    path('actualizar/<int:id>/', actualizar_usu, name='actualizar_usu'),
    path('login/', login, name='login'),
    path('usuario/', insetar_usuario, name='insetar_usuario'),


]
