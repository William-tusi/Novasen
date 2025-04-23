# Novasen_app/urls/auth_urls.py
from django.urls import path
from Novasen_app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registrar, name="registro"),
    path('usuario/perfil/', perfil, name="perfil_usuario"),
    path('login/usuario/', login, name="login_usuario"),
    path('usuario/', insetar_usuario, name='insetar_usuario'),
    
   
]
