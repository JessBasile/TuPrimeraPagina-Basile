from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from usuarios.forms import MiFormularioDeCreacion, MiFormularioDeEdicion, MiCambioPassword
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
                usuario = formulario.get_user()
                
                django_login(request, usuario)
                
                InfoExtra.objects.get_or_create(user=usuario)
                
                return redirect('inicio')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
                
            return redirect('login')
    else:
        formulario = MiFormularioDeCreacion()
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def editar_perfil(request):
    
    info_extra = request.user.infoextra
     
    if request.method == 'POST':
        formulario = MiFormularioDeEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
                
            if formulario.cleaned_data.get('asignatura'):
                info_extra.asignatura = formulario.cleaned_data.get('asignatura')
                
            info_extra.save()
        
            formulario.save()
                
            return redirect('inicio')
    else:
        formulario = MiFormularioDeEdicion(instance=request.user, initial={'avatar' : info_extra.avatar, 'asignatura' : info_extra.asignatura})
        
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

def informacion_perfil(request):
    usuario = request.user
    return render(request, 'usuarios/informacion_perfil.html', {'usuario': usuario})

# CLASE BASADA EN VISTA
class CambioPassword(PasswordChangeView):
    form_class = MiCambioPassword #Se incorpora para mejorar el formulario del template
    template_name = 'usuarios/cambio_pass.html'
    success_url = reverse_lazy('inicio')