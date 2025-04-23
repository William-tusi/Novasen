from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.provivencia_models import Provivencia  # ✅ correcto

def insertar_provivencia(request):
    if request.method == "POST":
        if request.POST.get("codigo") and request.POST.get("provivencia"):
            provincia = Provivencia()
            provincia.codigo = request.POST.get("codigo")
            provincia.provincia = request.POST.get("provivencia")
            provincia.save()
            return redirect('listar_provivencia')
    else:
        return render(request, "provivencia/insertar_provivencia.html")

def listar_provivencia(request):
    provivencia = Provivencia.objects.all()
    return render(request, 'provivencia/listar_provivencia.html', {'provivencia': provivencia})

def actualizar_provivencia(request, id):
    provivencia = get_object_or_404(Provivencia, id=id)
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['codigo', 'provivencia']):
            provivencia.codigo = request.POST.get('codigo')
            provivencia.provincia = request.POST.get('provivencia')
            provivencia.save()
            return redirect('listar_provivencia')
    else:
        return render(request, 'provivencia/actualizar_provivencia.html', {'provivencia': provivencia})

def eliminar_provivencia(request, id):
    provincia = get_object_or_404(Provivencia, id=id)
    provincia.delete()
    return redirect('listar_provivencia')
