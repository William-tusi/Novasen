from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.ambiente_models import Ambiente  # ✅ Import correcto
from Novasen_app.models.fichas_models import Fichas      # ✅ Import correcto

def insertar_ficha(request):
    if request.method == "POST":
        if (request.POST.get("ficha")
            and request.POST.get("nombre")
            and request.POST.get("ambientes_id")):
            
            ficha = Fichas()
            ficha.ficha = request.POST.get("ficha")
            ficha.nombre = request.POST.get("nombre")
            
            ambientes_id = request.POST.get("ambientes_id")
            ficha.ambiente = Ambiente.objects.get(id=ambientes_id)

            ficha.save()
            return redirect("listar_ficha")

    else:
        ambientes = Ambiente.objects.all()
        return render(request, "fichas/insertar_ficha.html", {'ambientes': ambientes})

def listar_ficha(request):
    fichas = Fichas.objects.all()
    return render(request, 'fichas/listar_ficha.html', {'ficha': fichas})

