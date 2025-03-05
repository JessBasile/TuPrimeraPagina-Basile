from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field: '' for field in fields}

class MiFormularioDeEdicion(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    asignatura = forms.CharField(label='Asignatura', required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

#Es agregado para mejorar el formulario del template y que no sea en inglés
class MiCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label="Contaseña Actual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput)