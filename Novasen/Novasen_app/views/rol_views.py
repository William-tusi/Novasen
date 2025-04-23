from django.shortcuts import render, get_object_or_404, redirect
from Novasen_app.models.rol_models import Rol  # ✅ Correcto, solo esta
from django.http import JsonResponse

def insertar_rol(request):
    if request.method == 'POST':
        if (request.POST.get('nombre') 
           and request.POST.get('codigo')
           and request.POST.get('descripcion')):

            rol = Rol()
            rol.nombre = request.POST.get('nombre')
            rol.codigo = request.POST.get('codigo')
            rol.descripcion = request.POST.get('descripcion')
            rol.save()
            return redirect('listar')
    else:
        return render(request, 'rol/insertar_rol.html')

def listar_rol(request):
    rol = Rol.objects.all()
    if request.headers.get('Accept') == 'application/json':
        data = {
            "title": "Listado de Roles",
            "body": [{"id": r.id, "nombre": r.nombre} for r in rol]
        }
        return JsonResponse(data)
    return render(request, 'rol/listar_rol.html', {'rol': rol})

def actualizar_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['nombre', 'descripcion']):
            rol.nombre = request.POST.get('nombre')
            rol.descripcion = request.POST.get('descripcion')
            rol.save()
            return redirect('listar_rol')
    else:
        return render(request, 'rol/actualizar_rol.html', {'rol': rol})

def eliminar_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    rol.delete()
    return redirect('listar_rol')
