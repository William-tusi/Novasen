from django.shortcuts import render, redirect, get_object_or_404
from Novasen_app.models import Usuario, Rol
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('bienvenida')
            else:
                form.add_error(None, 'Credenciales incorrectas')
    else:
        form = AuthenticationForm()
    return render(request, 'usuario/login.html', {'form': form})


def insertar_usuario(request):
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ["tipo_doc", "num_doc", "first_name", "last_name", "username", "email", "password", "telefono", "rol_id"]):
            Usuario.objects.create_user(
                tipo_doc=request.POST.get('tipo_doc'),
                num_doc=request.POST.get('num_doc'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                username=request.POST.get('username'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
                telefono=request.POST.get('telefono'),
                rol=Rol.objects.get(id=request.POST.get('rol_id'))
            )
        return redirect('listar_usu')
    roles = Rol.objects.all()
    return render(request, 'usuario/insertar_usuario.html', {'roles': roles})

def listar_usu(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar_usu.html', {'usuario': usuarios})

def actualizar_usu(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['tipo_doc', 'num_doc', 'first_name', 'last_name', 'username', 'email', 'password', 'telefono']):
            usuario.tipo_doc = request.POST.get("tipo_doc")
            usuario.num_doc = request.POST.get("num_doc")
            usuario.first_name = request.POST.get("first_name")
            usuario.last_name = request.POST.get("last_name")
            usuario.username = request.POST.get("username")
            usuario.email = request.POST.get("email")
            usuario.password = request.POST.get("password")
            usuario.telefono = request.POST.get("telefono")
            usuario.save()
            return redirect('listar_usu')
    return render(request, 'usuario/actualizar_usu.html', {'usuario': usuario})

def eliminar_usu(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('listar_usu')
from django.shortcuts import render

