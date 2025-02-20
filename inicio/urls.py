from inicio.views import inicio, saludo, crear_alumno, listado_de_alumnos
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear-alumno/', crear_alumno, name='crear_alumno'),
    path('listado-de-alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
]