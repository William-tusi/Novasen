from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import viewsets

from Novasen_api.models import (
    Rol, Usuario, Provincia, Ciudad, Sedes, Programas, Fichas,
    Regional, Ambiente
)
from .serializer import ProgramasSerializer


# Sesión
@login_required
def bienvenida(request):
    return render(request, 'sesion/bienvenido.html')

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('bienvenida')
            else:
                form.add_error(None, 'Credenciales incorrectas')
    else:
        form = AuthenticationForm()
    return render(request, 'sesion/login.html', {'form': form})

def registrar(request):
    return render(request, 'registro.html')


# Roles
def insertar(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('codigo') and request.POST.get('descripcion'):
            Rol.objects.create(
                nombre=request.POST.get('nombre'),
                codigo=request.POST.get('codigo'),
                descripcion=request.POST.get('descripcion')
            )
        return redirect('listar')
    return render(request, 'rol/insertar.html')

def listar(request):
    roles = Rol.objects.all()
    if request.headers.get('Accept') == 'application/json':
        data = {
            "title": "Listado de Roles",
            "body": [{"id": r.id, "nombre": r.nombre} for r in roles]
        }
        return JsonResponse(data)
    return render(request, "rol/listar.html", {"rol": roles})

def actualizar_rol(request, id):
    rol = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('descripcion'):
            rol.nombre = request.POST.get('nombre')
            rol.descripcion = request.POST.get('descripcion')
            rol.save()
            return redirect('listar')
    return render(request, 'rol/actualizar.html', {'rol': rol})

def eliminar_rol(request, id):
    get_object_or_404(Rol, id=id).delete()
    return redirect('listar')


# Usuarios
def insertar_usuario(request):
    if request.method == 'POST':
        campos = ['tipo_doc', 'num_doc', 'first_name', 'last_name', 'username', 'email', 'password', 'telefono', 'rol_id']
        if all(request.POST.get(campo) for campo in campos):
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
        campos = ['tipo_doc', 'num_doc', 'first_name', 'last_name', 'username', 'email', 'password', 'telefono']
        if all(request.POST.get(campo) for campo in campos):
            for campo in campos:
                setattr(usuario, campo, request.POST.get(campo))
            usuario.save()
            return redirect('listar_usu')
    return render(request, 'usuario/actualizar_usu.html', {'usuario': usuario})

def eliminar_usu(request, id):
    get_object_or_404(Usuario, id=id).delete()
    return redirect('listar_usu')


# Provincias
def insertar_provincia(request):
    if request.method == 'POST':
        if request.POST.get("codigo") and request.POST.get("provincia"):
            Provincia.objects.create(
                codigo=request.POST.get("codigo"),
                provincia=request.POST.get("provincia")
            )
            return redirect('listar_provincia')
    return render(request, "provincia/insertar_provincia.html")

def listar_provincia(request):
    provincias = Provincia.objects.all()
    return render(request, 'provincia/listar_provincia.html', {'provincia': provincias})

def actualizar_provincia(request, id):
    provincia = get_object_or_404(Provincia, id=id)
    if request.method == 'POST':
        if request.POST.get("codigo") and request.POST.get("provincia"):
            provincia.codigo = request.POST.get("codigo")
            provincia.provincia = request.POST.get("provincia")
            provincia.save()
            return redirect('listar_provincia')
    return render(request, 'provincia/actualizar_prov.html', {'provincia': provincia})

def eliminar_provincia(request, id):
    get_object_or_404(Provincia, id=id).delete()
    return redirect('listar_provincia')


# Ciudades
def insertar_ciudad(request):
    if request.method == 'POST':
        if request.POST.get('codigo') and request.POST.get('ciudad') and request.POST.get('provincias_id'):
            Ciudad.objects.create(
                codigo=request.POST.get("codigo"),
                ciudad=request.POST.get("ciudad"),
                provincia=Provincia.objects.get(id=request.POST.get("provincias_id"))
            )
            return redirect('listar_ciu')
    provincias = Provincia.objects.all()
    return render(request, 'ciudad/insertar_ciudad.html', {'provincias': provincias})

def listar_ciu(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'ciudad/listar_ciu.html', {'ciudad': ciudades})

def actualizar_ciu(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    if request.method == 'POST':
        if request.POST.get("codigo") and request.POST.get("ciudad"):
            ciudad.codigo = request.POST.get("codigo")
            ciudad.ciudad = request.POST.get("ciudad")
            ciudad.save()
            return redirect('listar_ciu')
    return render(request, 'ciudad/actualizar_ciu.html', {'ciudad': ciudad})

def eliminar_ciu(request, id):
    get_object_or_404(Ciudad, id=id).delete()
    return redirect('listar_ciu')


# Sedes
def insertar_sedes(request):
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['codigo', 'nombre', 'direccion', 'regional_id']):
            Sedes.objects.create(
                codigo=request.POST.get("codigo"),
                nombre=request.POST.get("nombre"),
                direccion=request.POST.get("direccion"),
                regional=Regional.objects.get(id=request.POST.get("regional_id"))
            )
            return redirect('listar_sedes')
    regionales = Regional.objects.all()
    return render(request, 'sede/insertar_sedes.html', {'regionales': regionales})

def listar_sedes(request):
    sedes = Sedes.objects.all()
    return render(request, 'sede/listar_sedes.html', {'sedes': sedes})

def actualizar_sedes(request, id):
    sede = get_object_or_404(Sedes, id=id)
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['codigo', 'nombre', 'direccion']):
            sede.codigo = request.POST.get("codigo")
            sede.nombre = request.POST.get("nombre")
            sede.direccion = request.POST.get("direccion")
            sede.save()
            return redirect('listar_sedes')
    return render(request, 'ciudad/actualizar_sedes.html', {'sedes': sede})

def eliminar_sedes(request, id):
    get_object_or_404(Sedes, id=id).delete()
    return redirect('listar_sedes')


# Programas
def insertar_programas(request):
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['codigo', 'nombre', 'horas', 'version', 'ficha_id']):
            Programas.objects.create(
                codigo=request.POST.get("codigo"),
                nombre=request.POST.get("nombre"),
                horas=request.POST.get("horas"),
                version=request.POST.get("version"),
                ficha=Fichas.objects.get(id=request.POST.get("ficha_id"))
            )
            return redirect('listar_programas')
    fichas = Fichas.objects.all()
    return render(request, 'programa/insertar_programas.html', {'fichas': fichas})

def listar_programas(request):
    programas = Programas.objects.all()
    return render(request, 'programa/listar_programas.html', {'programas': programas})

class ProgramasViewset(viewsets.ModelViewSet):
    queryset = Programas.objects.all()
    serializer_class = ProgramasSerializer


# Fichas
def insertar_ficha(request):
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['ficha', 'nombre', 'ambientes_id']):
            Fichas.objects.create(
                ficha=request.POST.get("ficha"),
                nombre=request.POST.get("nombre"),
                ambiente=Ambiente.objects.get(id=request.POST.get("ambientes_id"))
            )
            return redirect('listar_ficha')
    ambientes = Ambiente.objects.all()
    return render(request, 'fichas/insertar_ficha.html', {'ambientes': ambientes})

def listar_ficha(request):
    fichas = Fichas.objects.all()
    return render(request, 'fichas/listar_ficha.html', {'ficha': fichas})


# Regionales
def insertar_regional(request):
    if request.method == 'POST':
        if all(request.POST.get(field) for field in ['nit', 'nombre', 'ciudad']):
            Regional.objects.create(
                nit=request.POST.get("nit"),
                nombre=request.POST.get("nombre"),
                ciudad=request.POST.get("ciudad")
            )
            return redirect('listar_regional')
    return render(request, 'regionales/insertar_regional.html')

def listar_regional(request):
    regionales = Regional.objects.all()
    return render(request, 'regionales/listar_regional.html', {'regional': regionales})


# Ambientes
def insertar_ambiente(request):
    if request.method == 'POST':
        if request.POST.get('piso') and request.POST.get('salon'):
            Ambiente.objects.create(
                piso=request.POST.get('piso'),
                salon=request.POST.get('salon')
            )
            return redirect('listar_ambiente')
    return render(request, 'ambientes/insertar_ambiente.html')

def listar_ambiente(request):
    ambientes = Ambiente.objects.all()
    return render(request, 'ambientes/listar_ambiente.html', {'ambiente': ambientes})
