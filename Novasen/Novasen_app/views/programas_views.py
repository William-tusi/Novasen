from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.programas_models import Programas  # ✅ Import correcto
from Novasen_app.models.fichas_models import Fichas        # ✅ Import correcto

def insertar_programas(request):
    if request.method == "POST":
        if (request.POST.get("codigo")
            and request.POST.get("nombre")
            and request.POST.get("horas")
            and request.POST.get("version")
            and request.POST.get('ficha_id')):

            programas = Programas()
            programas.codigo = request.POST.get("codigo")
            programas.nombre = request.POST.get("nombre")
            programas.horas = request.POST.get("horas")
            programas.version = request.POST.get("version")
            
            ficha_id = request.POST.get("ficha_id")
            try:
                programas.ficha = Fichas.objects.get(id=ficha_id)
            except Fichas.DoesNotExist:
                return redirect('listar_programas')
           
            programas.save() 
            return redirect("listar_programas")
    
    else:
        fichas = Fichas.objects.all()
        return render(request, "programa/insertar_programas.html", {'fichas': fichas})

def listar_programas(request):
    programas = Programas.objects.all()
    return render(request, 'programa/listar_programas.html', {'programas': programas})
