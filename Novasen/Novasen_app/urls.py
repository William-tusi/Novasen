# novasen_app/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Otras rutas de tu aplicación...
]
