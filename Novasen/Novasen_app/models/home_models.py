from django.shortcuts import render

def perfil(request):
    return render(request, 'perfil.html')

def registrar(request):
    return render(request, 'registrar.html')

def home(request):
    return render(request, 'home.html')


