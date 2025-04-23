from django.urls import path
from Novasen_app.views.fichas_views import insertar_ficha, listar_ficha

urlpatterns = [
    path('insertar_ficha/', insertar_ficha, name='insertar_ficha'),
    path('listar_ficha/', listar_ficha, name='listar_ficha'),
]
