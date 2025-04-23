from django.urls import path
from Novasen_app.views.ciudad_views import insertar_ciudad,listar_ciudad,eliminar_ciudad,actualizar_ciudad

urlpatterns = [
    path('insertar/', insertar_ciudad, name='insertar_ciudad'),
    path('listar/', listar_ciudad, name='listar_ciudad'),
    path('ciudad/eliminar/<int:id>',eliminar_ciudad, name='eliminar_ciudad'),
    path('ciudad/actualizar/<int:id>',actualizar_ciudad, name='actualizar_ciu'),
]
