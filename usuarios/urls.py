from django.urls import path
from usuarios.views import login, registro, editar_perfil, informacion_perfil, CambioPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('editar-perfil', editar_perfil, name='editar_perfil'),
    path('informacion-perfil', informacion_perfil, name='informacion_perfil'),
    path('editar-perfil/cambiar-pass/', CambioPassword.as_view(), name='cambiar_pass'),
]