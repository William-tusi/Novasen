from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.ciudad_models import Ciudad         # ✅ correcto
from Novasen_app.models.provivencia_models import Provivencia  # ✅ correcto
from Novasen_app.models.sedes_models import Sedes# ✅ correcto

def insertar_ciudad(request):
    if request.method == 'POST':
        if request.POST.get('codigo') and request.POST.get('ciudad') and request.POST.get('provincia_id'):
            ciudad = Ciudad()
            ciudad.codigo = request.POST.get('codigo')
            ciudad.ciudad = request.POST.get('ciudad')
            provincia_id = request.POST.get('provincia_id')
            ciudad.provincia = Provivencia.objects.get(id=provincia_id)
            ciudad.save()
            return redirect('listar_ciudad')
    provincias = Provivencia.objects.all()
    return render(request, 'ciudad/insertar_ciudad.html', {'provincias': provincias})

def listar_ciudad(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'ciudad/listar_ciudad.html', {'ciudades': ciudades})

def actualizar_ciudad(request, id):
    ciudad = get_object_or_404(Sedes, id=id)
    if request.method == 'POST':
        campos_obligatorios=['codigo','nombre']
        if all (request.POST.get(field)for field in campos_obligatorios):
               
            ciudad.codigo = request.POST.get("codigo")
            ciudad.nombre = request.POST.get("ciudad")
            ciudad.save()
            return redirect ('listar_ciudad')
    else:
        return render (request, 'ciudad/actualizar_ciu.html',{'ciudad': ciudad})
         
def eliminar_ciudad(request,id):
     ciudad= get_object_or_404(Ciudad, id=id)
     ciudad.delete()
     return redirect ('listar_ciu')