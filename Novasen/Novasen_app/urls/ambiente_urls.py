from django.urls import path
from Novasen_app.views.ambiente_views import insertar_ambiente, listar_ambiente

urlpatterns = [
    path('insertar/', insertar_ambiente, name='insertar_ambiente'),
    path('listar/', listar_ambiente, name='listar_ambiente'),
]
