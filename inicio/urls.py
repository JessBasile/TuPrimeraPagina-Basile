from inicio.views import inicio, saludo, crear_alumno, listado_de_alumnos, ver_alumno, eliminar_alumno, ModificarAlumnoVista, EliminarAlumnoVista
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo'),
    path('crear-alumno/', crear_alumno, name='crear_alumno'),
    path('listado-de-alumnos/', listado_de_alumnos, name='listado_de_alumnos'),
    path('ver-alumno/<int:alumno_id>/', ver_alumno, name='ver_alumno'),
    # VISTAS COMUNES
    # path('modificar-alumno/<int:alumno_id>', modificar_alumno, name='modificar_alumno'),
    # path('eliminar-alumno/<int:alumno_id>/', eliminar_alumno, name='eliminar_alumno'),
    # CLASES BASADAS EN VISTAS (CBV)
    path('modificar-alumno/<int:pk>', ModificarAlumnoVista.as_view(), name='modificar_alumno'),
    path('eliminar-alumno/<int:pk>/', EliminarAlumnoVista.as_view(), name='eliminar_alumno'),
]