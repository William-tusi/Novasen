from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.regional_models import Regional  # ✅ Import correcto

def insertar_regional(request):
    if request.method == "POST":
        if request.POST.get("nit") and request.POST.get("nombre") and request.POST.get("ciudad"):
            regional = Regional()
            regional.nit = request.POST.get("nit")
            regional.nombre = request.POST.get("nombre")
            regional.ciudad = request.POST.get("ciudad")
            regional.save()
            return redirect('listar_regional')
    else:
        return render(request, "regionales/insertar_regional.html")

def listar_regional(request):
    regionales = Regional.objects.all()
    return render(request, 'regionales/listar_regional.html', {'regional': regionales})
