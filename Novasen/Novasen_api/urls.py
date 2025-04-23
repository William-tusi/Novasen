# urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_namespace'),
    path('api-docs/', include('rest_framework.urls'), name='api_docs_namespace'),
    
    # URLs para la aplicación Novasen
    path('Novasen/', include('Novasen_app.urls')),  # Enlaza las URLs de la app 'novasen_app'
    
    # URLs para la API Novasen
    path('Novasen-api/', include('Novasen_api.urls')),  # Enlaza las URLs de la API 'novasen_api'
    path('some_endpoint/', views.some_view, name='some_endpoint'),
]
