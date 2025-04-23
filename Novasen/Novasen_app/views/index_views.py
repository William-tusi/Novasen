# Novasen_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'login/perfil.html')

def home(request):
    return render(request, 'index.html')

def insetar_usuario(request):
    # Lógica para registrar al usuario
    return render(request, 'usuario/insertar_usuario.html')

def registrar(request):
    return render(request, 'registro.html')
