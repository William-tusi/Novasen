"""
URL configuration for gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Novasen_app.views import * 
from django.contrib.auth import views as auth_views

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name="home" ),
    
    path('insertar_rol', insertar_rol, name='insertar'),
    path('listar_rol', listar_rol, name='listar'),
    path('rol/eliminar/<int:id>',eliminar_rol, name='eliminar_rol'),
    path('rol/actualizar/<int:id>' ,actualizar_rol, name='actualizar_rol'),

    path('insertar_usuario', insertar_usuario, name="insertar_usuario"),
    path('listar_usu',listar_usu, name='listar_usu'),
    path('usuario/eliminar/<int:id>',eliminar_usu, name='eliminar_usu'),
    path('usuario/actualizar/<int:id>',actualizar_usu, name='actualizar_usu'),

    path('insertar_ciudad',insertar_ciudad, name='insertar_ciudad'),
    path('listar_ciu', listar_ciudad, name='listar_ciu'),
    path('ciudad/eliminar/<int:id>',eliminar_ciudad, name='eliminar_ciu'),
    path('ciudad/actualizar/<int:id>',actualizar_ciudad, name='actualizar_ciu'),

    path('insertar_sedes',insertar_sedes, name='insertar_sedes'),
    path('listar_sedes', listar_sedes, name='listar_sedes'),
    path('sedes/eliminar/<int:id>',eliminar_sedes, name='eliminar_sedes'),
    path('sedes/actualizar/<int:id>',actualizar_sedes, name='actualizar_sedes'),

    path('insertar_provivencia',insertar_provivencia, name='insertar_provivencia'),
    path('listar_provincia', listar_provivencia, name='listar_provivencia'),
    path('provivencia/eliminar/<int:id>',eliminar_provivencia, name='eliminar_provivencia'),
    path('provivencia/actualizar/<int:id>',actualizar_provivencia, name='actualizar_provievncia'),

    path('insertar_programas',insertar_programas, name='insertar_programas'),
    path('listar_programas', listar_programas, name='listar_programas'),

    path('insertar_ficha',insertar_ficha, name='insertar_ficha'),
    path('listar_ficha', listar_ficha, name='listar_ficha'),

    path('insertar_regional', insertar_regional, name='insertar_regional'),
    path('listar_regional', listar_regional, name='listar_regional'),

    path('insertar_ambiente', insertar_ambiente, name='insertar_ambiente'),
    path('listar_ambiente', listar_ambiente, name='listar_ambiente'),
    
    path('registrar/', registrar, name='register'), 

    #login
    path('login',login, name='login'),
    path('perfil', perfil, name='perfil'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    
    path('docs/',include_docs_urls(title='Documentation Rest Usuario')),
   
    
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

]
