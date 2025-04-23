from django.urls import path
from Novasen_app.views.regional_views import insertar_regional, listar_regional

urlpatterns = [
    path('insertar/', insertar_regional, name='insertar_regional'),
    path('listar/', listar_regional, name='listar_regional'),
]
