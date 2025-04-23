from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models import *
from django.contrib.auth.forms import AuthenticationForm


def insertar_sedes(request):
    if request.method == "POST":
        if (request.POST.get("codigo") and
            request.POST.get("nombre") and
            request.POST.get("direccion") and
            request.POST.get("regional_id")):

            sede = Sedes()
            sede.codigo = request.POST.get("codigo")
            sede.nombre = request.POST.get("nombre")
            sede.direccion = request.POST.get("direccion")
            regional_id = request.POST.get("regional_id")
            sede.regional = Regional.objects.get(id=regional_id)
            sede.save()
            return redirect("listar_sedes")
    else:
        regionales = Regional.objects.all()
        return render(request, "sede/insertar_sedes.html", {"regionales": regionales})


def listar_sedes(request):
    sedes = Sedes.objects.all()
    return render(request, 'sede/listar_sedes.html', {'sedes': sedes})


def actualizar_sedes(request, id):
    sedes = get_object_or_404(Sedes, id=id)
    if request.method == 'POST':
        campos_obligatorios = ['codigo', 'nombre', 'direccion', 'regional_id']
        if all(request.POST.get(field) for field in campos_obligatorios):
            sedes.codigo = request.POST.get("codigo")
            sedes.nombre = request.POST.get("nombre")
            sedes.direccion = request.POST.get("direccion")
            regional_id = request.POST.get("regional_id")
            sedes.regional = Regional.objects.get(id=regional_id)
            sedes.save()
            return redirect('listar_sedes')
    else:
        regionales = Regional.objects.all()
        return render(request, 'sede/actualizar_sedes.html', {'sedes': sedes, 'regionales': regionales})


def eliminar_sedes(request, id):
    sedes = get_object_or_404(Sedes, id=id)
    sedes.delete()
    return redirect('listar_sedes')
