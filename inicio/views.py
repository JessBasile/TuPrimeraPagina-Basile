from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Alumno
from inicio.forms import CrearAlumno, BuscarAlumno, ModificarAlumno
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    # return HttpResponse("<h1>Bienvenido/a</h1>")
    return render(request, 'inicio/inicio.html')

def saludo(request, nombre, apellido):
    hora_actual = datetime.now()
    return render(request, 'inicio/saludo.html', {'hora' : hora_actual, 'nombre' : nombre, 'apellido' : apellido})

def crear_alumno(request):
    print(request.GET)
    print(request.POST)
    
    formulario = CrearAlumno()
    error = ""
    
    if request.method == "POST":
        formulario = CrearAlumno(request.POST, request.FILES)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            email = formulario.cleaned_data.get('email')
            institucion = formulario.cleaned_data.get('institucion')
            materia = formulario.cleaned_data.get('materia')
            fecha_creacion = formulario.cleaned_data.get('fecha_creacion')
            avatar_alumno = formulario.cleaned_data.get('avatar_alumno')
            
            if Alumno.objects.filter(email=email).exists():
                error = "Este corre electrónico ya se encuentra registrado"
                print("⚠ ERROR:", error)
            else:                    
                alumno = Alumno(nombre=nombre, apellido=apellido, email=email, institucion=institucion, materia=materia, fecha_creacion=fecha_creacion, avatar_alumno=avatar_alumno)
                alumno.save()
            
                return redirect("listado_de_alumnos")
            
    return render(request, 'inicio/crear_alumno.html', {'formulario': formulario, 'error': error})

def listado_de_alumnos(request):
    alumnos = Alumno.objects.all()
    formulario = BuscarAlumno(request.GET)
    if formulario.is_valid():
        institucion = formulario.cleaned_data.get('institucion')
        materia = formulario.cleaned_data.get('materia')
        
        if institucion:
            alumnos = alumnos.filter(institucion__icontains=institucion)
        if materia:
            alumnos = alumnos.filter(materia__icontains=materia)
    return render(request, 'inicio/listado_de_alumnos.html', {'alumnos': alumnos, 'formulario': formulario})

@login_required
def ver_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    return render(request, 'inicio/ver_alumno.html', {'alumno': alumno})

# VISTAS COMUNES
def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    alumno.delete()
    return redirect('listado_de_alumnos')

def modificar_alumno(request, alumno_id):
    
    alumno = Alumno.objects.get(id=alumno_id)

    if request.method == "POST":
        formulario = ModificarAlumno(request.POST, request.FILES, instance=alumno)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar_alumno'):
                alumno.avatar_alumno = formulario.cleaned_data.get('avatar_alumno')
            alumno.save()
            return redirect('listado_de_alumnos')
    else:
        formulario = ModificarAlumno(instance=alumno)
        
    return render(request, 'inicio/modificar_alumno.html', {'formulario': formulario})

# CLASES BASADAS EN VISTAS
class ModificarAlumnoVista(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = "inicio/CBV/modificar_alumno.html"
    # fields = "__all__"
    form_class = ModificarAlumno
    success_url = reverse_lazy('listado_de_alumnos')
    
class EliminarAlumnoVista(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = "inicio/CBV/eliminar_alumno.html"
    success_url = reverse_lazy('listado_de_alumnos')