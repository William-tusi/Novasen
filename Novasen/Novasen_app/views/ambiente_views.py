from django.shortcuts import render, redirect
from Novasen_app.models.ambiente_models import Ambiente

# Vista para insertar ambiente
def insertar_ambiente(request):
    if request.method == "POST":
        if request.POST.get('piso') and request.POST.get('salon'):
            ambiente = Ambiente()
            ambiente.piso = request.POST.get('piso')
            ambiente.salon = request.POST.get('salon')
            ambiente.save()
            return redirect("listar_ambiente")
    return render(request, "ambientes/insertar_ambiente.html")

# Vista para listar los ambientes
def listar_ambiente(request):
    ambientes = Ambiente.objects.all()
    return render(request, 'ambientes/listar_ambiente.html', {'ambientes': ambientes})
