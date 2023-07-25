from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from datetime import datetime
from django.contrib import messages

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return  render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    if request.method == 'POST':
        formulario = LibroForm(request.POST or None, request.FILES or None) #Identifica todos los archivos que van al formulario y los que se envian
        if formulario.is_valid():
            formulario.save()
            return redirect('libros')
    else:
        formulario = LibroForm()
            
    return render(request, 'libros/crear.html', {'formulario': formulario}) 


def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros') #Elimina el campo

def registro_usuarios(request):
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('ingreso_usuarios')
    else:
        formulario = RegistroUsuarioForm()

    return render(request, 'registros_usuarios.html', {'formulario': formulario})

def ingreso_usuarios(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            messages.success(request, 'Ingresaste con éxito!!!')
            return redirect('inicio.html')  # Reemplaza 'pagina_inicio' con la URL de tu página de inicio
    else:
        formulario = AuthenticationForm()

    return render(request, 'ingreso_usuarios.html', {'formulario': formulario})

def nosotros(request):
    current_year = datetime.now().year
    return render(request, 'paginas/nosotros.html', {'current_year': current_year})