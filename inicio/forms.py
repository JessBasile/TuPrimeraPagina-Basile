from django import forms
from inicio.models import Alumno

class CrearAlumno(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    institucion = forms.CharField(max_length=50)
    materia = forms.CharField(max_length=50)
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    avatar_alumno = forms.ImageField(required=False)
    
class BuscarAlumno(forms.Form):
    institucion = forms.CharField(max_length=50, required=False)
    materia = forms.CharField(max_length=50, required=False)
    
class ModificarAlumno(forms.ModelForm):
    fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    avatar_alumno = forms.ImageField(required=False)
    class Meta:
        model = Alumno
        fields = "__all__"