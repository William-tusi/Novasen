from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Novasen_app.views import home
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Administrador
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('api/', include('Novasen_app.urls')),


    path('', include('Novasen_app.urls')),

    path('app/', include('Novasen_app.urls')),
    # Rutas generales de la aplicación
    path('', include('Novasen_app.urls.general_urls')),

    # Gestión de roles
    path('roles/', include('Novasen_app.urls.rol_urls')),

    # Gestión de usuarios
    path('usuarios/', include('Novasen_app.urls.user_urls')),

    # Gestión de provincias
    path('provivencias/', include('Novasen_app.urls.provivencia_urls')),

    # Gestión de ciudades
    path('ciudades/', include('Novasen_app.urls.ciudad_urls')),

    # Gestión de sedes
    path('sedes/', include('Novasen_app.urls.sedes_urls')),

    # Gestión de programas
    path('programas/', include('Novasen_app.urls.programas_urls')),

    # Gestión de fichas
    path('fichas/', include('Novasen_app.urls.fichas_urls')),

    # Gestión de ambientes
    path('ambientes/', include('Novasen_app.urls.ambiente_urls')),

    # Documentación de la API
    path('docs/', include_docs_urls(title='Documentation Rest Usuario')),

    path('login/', include('Novasen_app.urls')),
]

# Para servir archivos estáticos y media en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
