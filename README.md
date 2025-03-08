## Proyecto de Página Web a través de Python con Django

<img align="right" alt="Python" width="250" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/python.gif">

El presente proyecto se basa en la creación de un sitio web basado en Python con la implementación del firmware Django, a través del editor Visual Studio Code.
Se espera que a través del sitio web se puedan ingresar datos por medio de un formulario, listar esos datos, buscar datos dentro de la base de datos creada anteriormente con otro formulario, loguearse y acceder a material de estudio acorde a la asignatura declarada por el usuario/estudiante. El siguiente video sintetiza la funcionalidad del sitio ([Link AQUÍ](https://www.youtube.com/watch?v=xt91jyZyDKE)).

1. **Configuración Inicial de Git y GitHub:**
Inicialmente se realiza la conexión y configuración de git al repositorio con los comandos correspondientes, antes de ello se recomienda configurar (y en caso que ya se haya efectuado) corroborar los datos de esa configuración global guardados en la carpeta de usuario:
```
git config --global user.name "Jesica Basile" # Para configurar el nombre de usuario
git config user.name # Para consultar el usuario configurado
git config --global user.email "jesica@example.com" # Para configurar el correo electrónico
git config user.email # Para consultar el correo electrónico configurado
git init # Inicialización de git y creación de repositorio local en la carpeta del proyecto, a la que git le hará seguimiento.
git status # permite realizar consultas para observar el estado de los cambios que se identifiquen
git add . # Agrega los cambios del área de working al de staging area
git commit -m "Descripción de los cambios" # Se utiliza para confirmar esos cambios y colocarles una descripción
git push origin main # Último paso que envía los cambios al repositorio de GitHub
```
Se pueden efectuar estas mismas configuraciones desde interface gráfica, pero en el caso del presente proyecto fue gestionado 100% desde la terminal. Se recomienda instalar la extensión `GitGraph` para observar el historial de cambios que fueron efectuados en la rama correspondiente desde el mismo Visual Studio Code.
Es importante, posicionarse en la "rama" adecuada en la que se desea trabajar en el repositorio, para evitar conflictos y versiones distintas en diferentes ubicaciones. La más común es main, y el posicionamiento en la misma se efectúa con el comando `git checkout main`, para ver todas las ramas `git branch` y para crear una nueva rama `git checkout -b nombre-de-la-rama`.

2. **Configuración del Gitignore:**
Antes de proceder a crear un entorno virtual que es recomendable para trabajar con django, será relevante configurar el archivo `.gitignore` para evitar pushear cambios al repositorio que no deseamos o que no es recomendable que sean visibles públicamente. Para ello, de un modo agilizado se recurre al sitio web `gitignore.io` seleccionando las tecnologías utilizadas y nos proporciona el contenido que deberá tener, este caso partícular la tecnologías seleccionadas serásn "Visual Studio Code", "Python" y "Django".

3. **Creación y uso de un entorno virtual:**
En este tipo de proyectos se recomienda la creación de un entorno virtual en el cual se instalen y manejen solo las dependencias o paquetes específicos que requiere el proyecto y no todos los paquetes globales instalados localmente. A continuación se detallan los comandos para su creación y activación:
```
python -m venv venv # Creación de un entorno virtual, tener en cuenta que ese nombre debe coincidir con lo que figura en gitignore para evitar que se suba al repositorio
source venv/bin/actívate # Activación del entorno virtual
```

4. **Instalación de Django:**

<img align="right" alt="Django" width="100" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/django-python-logo.png">

Se recomienda activar el entorno virtual y proceder a instalar django para hacerlo dentro del entorno:
```
pip install django # Para instalarse Django en el entorno virtual
pip freeze # Para observar los paquetes que tiene instalado el entorno (para ello ya debe estar activado el mismo)
```
Cada vez que se abra el proyecto en Visual Studio Code, se deberá activar el entorno virtual para que los cambios impacten adecuadamente en el proyecto.

5. **Creación y configuración del archivo requirements.txt:**
El archivo `requirements.txt` es necesario para listar todas las dependencias que el proyecto necesita y se configura con el siguiente comando:
```
pip freeze > requirements.txt
```
En el presente proyecto los paquetes recomendables son los siguientes:
```
asgiref==3.8.1
Django==5.1.6
pillow==11.1.0
sqlparse==0.5.3
tzdata==2025.1
```
En el caso que otro usuario descargue el proyecto, deberá crear su propio entorno local y ejecutar el comando `pip install -r requirements.txt` para instalar los paquetes que se necesitan en el nuevo entorno creado.

6. **Inicialización del Proyecto con Django:**
Se procede a iniciar el proyecto con Django ejecutando un comando que permite la creación de la estructura básica del proyecto con una carpeta (en este caso proyectoDjango), creandosé archivos clave como `manage.py` y `settings.py`.
```
django-admin startproject proyectoDjango .
```
El `.` al final colabora para que el archivo `manage.py` sea creado en la carpeta raíz del proyecto, y además, la carpeta se garantiza que la carpeta proyectoDjango contenga su archivo de `settings.py` (que contendrá las configuraciones por defecto de nuestro proyecto).

7. **Iniciar Servidor de desarrollo de Django con Python:**
El proyecto utilizará diferentes `URLs` para acceder a distintas `vistas` a través del navegador. Las vistas se encargan de la lógica de la aplicación, interactuando con los `modelos` (que representan la estructura de la base de datos) y los `templates` (archivos HTML que muestran la información al usuario).
Para poder crear esos archivos para cumplir las distintas finalidades, primero se deberá iniciar el servidor de desarrollo Django - generalmente - en la dirección `http://127.0.0.1:8000/` con la ejecución del siguiente comando:
```
python manage.py migrate
```
La primera vez que ejecuta ese comando, Django crea automáticamente una base de datos SQLite (`db.sqlite3`) con la aplicación de migraciones que aseguran la estructura de la base. El archivo deberá estar "oculto" por encontrarse mencionado dentro del archivo .gitignore. En futuras ejecusiones, no se crea una nueva base de datos, sino que el servidor simplemente utiliza la existente.
Cada vez que se procedan a realizar modificaciones se deberá activar el entorno virtual y posteriormente correr el servidor para poder ir guardando los cambios del proyecto adecuadamente. El siguiente comando hará correr el servidor Django:
```
python manage.py runserver
```

8. **Creación de una vista en una aplicación:**
Dentro del archivo urls.py se crea una aplicación `inicio` con el siguiente comando:
```
python manage.py startapp inicio
```
Esto crea una carpeta de inicio con todos los archivos correspondientes.
Posteriormente, se procede a crear una vista desde el archivo `views.py` dentro de la carpeta `inicio` con la siguiente linea de código:
```
def inicio(request):
    return render(request, 'inicio/inicio.html')
```
Aunque, dentro del mismo archivo se deberá importar una clase para que la vista funcione adecuadamente, con el siguiente comando:
```
from django.http import HttpResponse
```
Para que se pueda acceder a la vista será necesario establecer path en el archivo urls.py dentro de la carpeta inicio, por consiguiente, primero se configurará el archivo urls.py importando path:
```
from inicio.views import inicio
from django.urls import path
```
Y luego, proceder a incluir el `PATH` en el urls.py especificamente dentro de urlpatterns, con la siguiente línea de código:
```
 path('', inicio, name='inicio')
```
Esto, a su vez, requerirá que en la carpeta de proyectoDjango, dentro del archivo urls.py se incluya el siguiente PATH:
```
path('', include('inicio.urls'))
```
Esto último asegura que las rutas definidas en la aplicación inicio sean accesibles desde la URL principal del proyecto.
Para poder incluirlo, a su vez, se requerirá importar:
```
from django.urls import path, include
```
Caso contrario, no funcionaría adecuadamente.

9. **Creación de templates:**
Para crear templates se incorpora una carpeta denominada `templates` en la raiz general y otra carpeta igual pero dentro de inicio. La carpeta de templates (dentro de inicio), contendrá en su interior, otra carpeta llamada inicio, y allí se alojarán todos los .html de esa aplicación específica.
Por otro lado, en el archivo settings.py dentro de la carpeta proyectoDjango se deberá configurar la dirección de los templates, con el siguiente código:
```
'DIRS': [BASE_DIR / 'templates'],
```
De ese modo, todo aquel que descargue el proyecto podrá visualizarlo sin problemas, en cambio, si queda la ruta de la carpeta local del ordenador no será adecuado.
Asimismo, será necesario incluir en las `INSTALED_APPS` a la aplicación inicio para que Django la reconozca del siguiente modo:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio'
]
```

10. **Creaciones de otras vistas dentro de la misma aplicación:**
Se proceden a crear otras vistas dentro de la misma aplicación para lo cual se realizarán los mismos pasos efectuados anteriormente para la primera vista (inicio). Por lo tanto, se configurará cada una de las nuevas vistas dentro de views.py con su nuevo nombre, crear un template dentro de templates/"nombre de la aplicación" con el mismo nombre que la vista .html y definir la url dentro del archivo urls.py importando y agregando su path.
En una de las vistas creadas en el presente proyecto se utilizaron diccionarios o contextos que se le proporcionan al template para que cargue correctamente cierta información como puede ser hora y fecha actual con `datetime.now()` o un formulario con `{formulario}`.

11. **Incorporación de navegación en los templates:**
En cada archivo .html se debe configurar un menú de navegación con hipervínculos, permitiendo el acceso a las distintas páginas del proyecto. Esto se logra utilizando la etiqueta <nav> y la función url de Django para generar las rutas dinámicamente a través del nombre que se les asignó. Ejemplo del código de la navegación sobre algunos templates a continuación:
```
    <nav>
        <a href={% url "inicio" %}>Inicio</a>
        <a href={% url "crear_alumno" %}>Registración</a>
        <a href={% url "listado_de_alumnos" %}>Listado</a>
    </nav>
```

12. **Diseño de Modelos:**
Los modelos se crean por cada aplicación mediante el archivo `models.py` dentro del cual se definen estructuras de la base de datos específicas para cada aplicación.
El archivo incialmente deberá realizar la importación correspondiente:
```
from django.db import models
```
La creación de los modelos son similar a las clases que contendrán atributos en los distintos campos (al igual que el caso de los formularios). Luego de su elaboración, se deberá "conectar" con la base de datos mediante el siguiente comando en terminal:
```
python manage.py makemigrations
```
De ese modo, se crea un archivo intermedio dentro de la carpeta migrations que se aloja en la carpeta de la aplicación (en este caso, inicio) denominado `0001_initial.py` y tendrá número ascendente por cada cambio que se migre. De todos modos, los cambios no se encuentran impactados todavía en la base y para ello se ejecutará el comando migrate que trasladará esas migraciones:
```
python manage.py migrate
```
Se podrán corroborar las migraciones en el archivo db.sqlite3.

`Aclaración Importante:` Para que la ejecución del comando sea exitosa y se migre a la base de datos será necesario que la aplicación se encuentre configurada en el archivo settings.py de la carpeta proyectoDjango y que figure en los `INSTALLED_APP`, caso contrario no detectará los cambios.

13. **Elaboración de formularios en las distintas vistas:**
Los formularios se implementan a través de los templates de cada vista y estarán basados en el modelo de la aplicación. Sin embargo, es recomendable crear un archivo `forms.py` dentro de la aplicación, donde se definan los diferentes formularios que se utilizarán en las distintas vistas correspondientes.
Si cada aplicación dentro del proyecto requiere formularios, lo ideal es que cada una tenga su propio archivo forms.py para organizar y mantener el código de manera más estructurada.
Para el caso del formulario para inserción de datos es bajo método `POST` con la siguiente estructura de creación en html:
```
<form action="" method="POST">
```
Es utilizado para enviar datos al servidor y guardarlos en la base.
Los datos no son visibles en la URL. Éste método también podrá ser utilizado para modificación y eliminación de datos.
Para el caso de los formularios destinados a consultas de datos, no se especifica el método, y por lo tanto, por default es `GET` cuya finalidad es consulta o filtrado de datos.
En el archivo views.py en la siguiente línea de configuración sobre el comportamiento de los datos proporcionados a través del formulario, se verifica que todos los campos cumplen con las caracteristicas especificadas en forms.py:
```
if formulario.is_valid():
```
Y en la sección `cleaned_data` se extraen los datos validados del formulario.
Por último, los templates que contienen formularios con condicionales utilizan `{& if %}`, `{% else %}`, `{% for %}`, etc.

14. **Herencia de templates:**
Para evitar la repetición de código en los templates, se implementa la `herencia de templates` y se recurre a utilizar un bootstrap de la página https://startbootstrap.com/ cuya estructura html se copia en un template denominado `template_base.html` dentro de la carpeta templates en la carpeta proyectoDjango; y dentro de inicio se "extrae" el archivo descargado de la web (dado que al momento de la descarga se encuentra comprimido). En síntesis, se extraen los archivos que esa plantilla elegida de bootstrap contiene dentro de una carpeta denominada `static` (en la carpeta de la aplicación inicio).
Una vez creado el template base, se procederá a borrar en cada template de cada aplicación el código que se repite en todas, dejando solo el contenido específico de cada página/template. Asimismo, se incroporará en reemplazo, al inicio de cada template la siguiente primera línea de código que "importará" el contenido base del template general/base:
```
{% extends "template_base.html" %}
```
Para que funcione exitosamente se incorpora un `block` en el template_base (antes que termine todo el HTML) para indicar que se incorporará contenido en otros templates, con el siguiente código:
```
    {% block contenido %} # inicio
    {% endblock contenido %} # final
```

15. **Creación de Formularios con ModelForm:**
Para permitir la edición de registros, se crea un formulario en forms.py utilizando `ModelForm` con una sub-clase dentro `Meta`, que permitirá efectuar modificaciones y otro tipo de acciones sobre los registros.
Luego se incorporan tres vistas (con sus correspondientes urls) para poder eliminar registros, ver registros/consultarlos y modificar esos registro. Asimismo, en listado_de_alumos.html se deberán incorporar los links que deriven a las urls con interactividad que ejecuten esa acción ya sea eliminar, modificar o solo consultar.
Para el caso específico de modificar el registro, se creará una nueva clase dentro de forms.py `"ModificarAlumno"` con `forms.ModelForm` y Meta que permitirá identificar cierta configuración de la cual se puede especificar un modelo "Alumno" que se deberá importar con:
```
from inicio.models import Alumno
```

16. **Clases basadas en vistas (CBV):**
Cuando se realizan clases basadas en vistas, se crea una nueva carpeta para alojar las mismas, denominada `CBV` dentro de la carpeta de templates ---> inicio (en este caso particular).  Dentro del archivo views.py se deberá primero importar: 
```
from django.views.generic.edit import UpdateView 
```
Para utilizar un tipo de clase que nos proporciona Django `UpdateView`, pero también se deberá importar:
```
from django.urls import reverse_lazy
```
Esta última, es una funcionalidad que permite hacer lo mismo que el redirect pero para un `success_url`. Por último, en el archivo modificar_alumno.html se debe reemplazar `{{form}}` en donde se utiliza {{formulario}} para que lo tome adecuadamente y en el PATH en urls:
``` 
path('modificar-alumno/<int:pk>', ModificarAlumnoVista.as_view(), name='modificar_alumno'),
```
En el caso del eliminado, se efectúan los mismos pasos solo que en lugar de importar UpdateView en django.views se importará `DeleteView`. **Para eliminar en el caso de CBV será necesario un template porque requerirá CONFIRMAR**.

17. **Incorporación en el models.py un campo fecha:**
En este caso particular, como la base de datos ya tiene datos cargados el nuevo campo (fecha) que se decide incorporar se lo efectúa con la caracteristica de ser nulo, para que de ese modo, no surjan inconvenientes con los registros cargados previamente a la modificación. La línea de código que se incorpora en la class Alumno es:
```
fecha_creacion = models.DataField(null=True)
```
y luego serán ejecutados los comandos:
```
python manage.py makemigrations
Python manage.py migrate
```
Django detectará el cambio en el modelo y generará una nueva migración denominada `0002_alumno_fecha_creacion.py` en la carpeta migrations en la aplicación inicio. Posteriormente deberá ser incorporada esa modificación en la views.py, en el forms.py y models.py.
En el caso del forms.py en la class CrearAlumno, se incorporará del siguiente modo:
```
fecha_creacion = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
```
Las modificaciones abordadas con el `widget` permite la aparición del formato de la fecha que tiene el campo que deberá ser completado, para enviar inconvenientes al usuario al momento de ingresar o modificar un registro.

18. **Creación de aplicación "USUARIOS":**
Inicialmente se crea una aplicación nueva con el siguiente código:
```
python manage.py startapp usuarios
```
Luego se debe incorporar en el archivo settings.py en la carpeta proyectoDjango en INSTALLED_APPS 'usuarios', y en urls.py de la misma carpeta incorporar el PATH en urlpatterns:
```
'usuarios',
```
Posteriormente, se deberá crear un archivo urls.py dentro de la nueva aplicación "usuarios" e incorporar la siguiente información:
```
from django.urls import path
from usuarios.views import login, registro

urlpatterns = [
    path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    # path('registro/', registro, name='registro'),
]
```
Y luego, configurar views.py de la carpeta usuarios.

19. **Login - Creación template sobre login:**
Se crean dos carpetas en el siguiente orden: templates/usuarios dentro de la aplicación usuarios. Posteriormente se creará el archivo `login.html` con el siguiente código:
```
{% extends "template_base.html" %}

<title>{% block title_head %}Login{% endblock title_head %}</title>

{% block contenido %}
<h2>Iniciar Sesión</h2>

    <form action="" method="POST">
        {% csrf_token %}
        {{formulario}}

        {% if error %}
        <p style="color: red;">{{ error }}</p>
        {% endif %}

        <input type="submit" value="Iniciar Sesion">    
    </form>
{% endblock contenido %}
```
Y en el template base, se colocará un "botón" para iniciar sesión, asi como también, información en la barra de navegación sobre el usuario cuando se encuentra logueado con la siguiente línea de código:
```
<li class="nav-item"><a class="nav-link js-scroll-trigger" href="#">{{request.user.username}}</a></li>
```
Asimismo, para poder realizar pruebas, se creará un `"super-usuario"` con las siguientes líneas de código directamente en terminal:
```
python manage.py createsuperuser
admin
```
La creación de ese super-usuario puede verificarse en la base de datos, y ya comenzará a figurar el nombre del usuario una vez que se encuentra logueado en la barra de navegación, tal como fue configurado.

20. **Logout:** 
En primer lugar, se realizará una importación de una CBV desde url.py ubicado en la aplicación usuarios:
```
from django.contrib.auth.views import LogoutView
```
y posteriormente el path de logout:
```
path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
```
Se creará un template `logout.html` que cuente solo con la leyenda que aclare que la sesión fue cerrada exitosamente y en el template base, se deberá incorporar un form con action que especifique la url logout, del siguiente modo:
```
<li class="nav-item">
                        <form action={% url "logout" %} method="POST">
                            {% csrf_token %}
                            <input class="btn btn-primary" style="background-color:rgb(239, 84, 53); color: black; border-color: #8B4513;" type="submit" value="Cerrar sesion">
                        </form>
                    </li>
```
De ese modo, Django proporciona un apartado especial denominado `"admin"` que no debería tener acceso un usuario "común", sino desarrolladores o personal capacitado que requiere utilizarlo (staff). Esto se logra mediante el link: http://127.0.0.1:8000/admin/login/?next=/admin/ en el que se observa la captura de la derecha y se podrán ingresar los datos del super-usuario creado.

<img align="right" alt="Python" width="250" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/django-admin.jpg">

Para poder visualizar la información de la base de datos correctamente en este apartado, se deberá importar en el archivo `admin.py` dentro de la aplicación inicio, lo siguiente:
```
from django.contrib import admin
from inicio.models import Alumno

# Register your models here.
admin.site.register(Alumno)
```
Las últimas dos lineas de código permiten registrar el modelo de alumnos y modelo para el manejo de usuarios/perfil.

21. **Implementación de mixin & decorador:**
El `mixin` SOLO podrá inplementarse en el caso de CBV y permitirá al usuario eliminar y modificar si y solo si está logueado. Para ellos, en la aplicación inicio, en el archivo de views.py se deberá importar:
```
from django.contrib.auth.mixins import LoginRequiredMixin
```
y luego en la misma ubicación se configurará la eliminación y modificación cambiando las siguientes líneas de código:
```
class ModificarAlumnoVista(LoginRequiredMixin, UpdateView):
class EliminarAlumnoVista(LoginRequiredMixin, DeleteView):
```
Es MUY importante que primero este el Mixin para que realmente NO permita efectuar cambios si no se está logueado. Finalmente, si el usuario intenta mientras no esté logueado, será derivado a la página de iniciar sesión con la finalidad de indicarle que debe efectuarlo. Para ello se agrega la siguiente línea de código al final del archivo settings.py en la carpeta de proyectoDjango:
```
LOGIN_URL = '/usuarios/login/'
```
En el caso que se trate de una vista general, NO se implementará mixin, sino, un `decorador`. Para ello, en el archivo views.py de la aplicación inicio, se importará:
```
from django.contrib.auth.decorators import login_required
```
Ese decorador se aplicará sobre una función/clase, en el presente proyecto se aplica sobre "ver más" información del siguiente modo:
```
@login_required # Se coloca antes de la función, para que impacte sobre la misma.
def ver_alumno(request, alumno_id):
```

22. **Aplicar cambios sobre "botones" de iniciar y cerrar sesión:**
Es recomendable que se vea uno u otro "botón" según la circunstancia, por ello se procede a efectuar algunos cambios que lo permitan. En el template_base se impletentará un if:
```
{% if  request.user.is_authenticated %}
```
De ese modo, si no está logueado aparecerá login y si ya está, figurará logout, pero nunca juntos en simultáneo.

23. **Registro de un usuario ("común") desde plataforma:**
Se incorpora en el template_base el "botón" para registrarse que solo figurará si el usuario no se encuentra logueado junto a iniciar sesión, por si ya se encuentra registrado.
Posteriormente, se incorpora la función de registro en views.py de la aplicación usuarios, aunque primero se deberá efectuar una importación:
```
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
```
Asimismo, para personalizar el formulario, se creará un archivo forms.py en la aplicación usuarios que dentro se importará y creará clases como a continuación:
```
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field: '' for field in fields}
```
Y por último, deberá ser importado el formulario en la vista del siguiente modo:
```
from usuarios.forms import MiFormularioDeCreacion
```

24. **Incorporación de información & edición de perfil:**
Se deberá crear una vista para edición de perfil dentro de la cual se podrá importar el `UserChangeForm` y será implementado para crear la función de la misma, aunque en el caso particular del presente proyecto, se utilizó un formulario de creación propia personalizado en forms.py dentro de la app usuarios. A su vez, se deberá incorporar el PATH en la urls y agregarlo en el template_base incorporando luego de loguearse esa posibilidad de edición del siguiente modo:
```
<li class="nav-item"><a class="nav-link js-scroll-trigger" href={% url "editar_perfil" %} style="color:rgba(228, 176, 119, 0.67)">{{request.user.username}}</a></li>
```
Asimismo, al momento de ingresar a la edición del perfil se incorporará (como buena práctica) una página `informacion_perfil.html` que muestre un detalle de la información actual del perfil, y un enlace, que derive a la `edicion_perfil.html`.
Por otro lado, se creará el apartado para el cambio de contraseña que se realizará en CBV importando desde django en views.py `PasswordChangeView`.

25. **Incorporación de cambio contraseña:**
Para lograr que el template del cambio de contraseña figure en español, y no en inglés como sucede por default, será recomendable armar una clase en forms.py dentro de la aplicación usuarios, que contenga:
```
class MiCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label="Contaseña Actual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput)
```
En conjunto, se deberá "llamar" en el formulario `{{form}}` dentro del template `cambio_pass.html` la url denominada `"cambiar_pass"` para que ese cambio de idioma se aplique exitosamente.

26. **Avatar:**
Para incorporar un avatar será necesario dentro de la aplicación usuarios, en models.py crear una clase `"InfoExtra"` determinando ese campo de imagen `"avatar"` del siguiente modo:
```
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blanck=True)
```
Posteriormente se deberrán ejecutar en terminal, todos los siguientes comandos:
```
pip install Pillow #Libreria necesaria para manejo de imágenes
pip freeze > requirements.txt
python manage.py makemigrations
Python manage.py migrate
```
Luego, se incorporarán en settings.py del proyecto las siguientes configuraciones o líneas de código:
```
import os
MEDIA_URL = '/media/'
MEDIA_ ROOT = os.path.join(BASE_DIR, 'media')
```
Y en urls.py del proyecto se incorporan importaciones y path:
```
from django.conf import settings
from django.conf.urls.static import static

    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
En consecuencia, se deberán reconfigurar las vistas de login y editar_perfil para incorporar esa InfoExtra del avatar requerida con la finalidad de ser guardadas adecuadamente. Y en el template de editar_perfil.html se modificará el formulario de la siguiente manera (ya no será simplemente POST):
```
    <form action={% url "editar_perfil" %} method="POST" enctype='multipart/form-data'>
```

27. **Incorporación de un nuevo campo en modelo InfoExtra:**
Se procede a modificar el modelo incorporando el campo `"asignatura"` para después en función de ese dato habilitar material de estudio según corresponda. Como esta modificación afecta la estructura de la base de datos se procederá a realizar `makemigrations` y `migrate` para actualizar la BD. 
Después se modificará la vista, y además, ese campo es incorporado en el formulario de edición para que el estudiante pueda completarlo, y luego, acceder a su material de estudio. Por último, se agrega en el template que muestra la información del usuario. 

28. **Incorporación de Avatar en aplicación Alumnos:**
Al igual que fué efectuado en los usuarios, se procede a incorporar un avatar en los alumnos. Primero se modifica el modelo agregando el avatar (y efectuando actualización de la BD con makemigrations y migrate), luego esa modificación es incorporada en la vista, el formulario y finalmente en el template.
En el modelo, se incorpora el avatar con la siguiente linea de código:
```
 avatar_alumno = models.ImageField(upload_to='avatares_alumnos', null=True, blank=True)
 ```
Posteriormente se modifican las vistas crear_alumno y modificar_alumno. En el caso particular de modificar_alumno se aplicarán las modificaciones sobre el template CBV que es el activo en el path de urls, caso contrario, no se aplicarán las modificaciones.
`Aclaración:` Sobre cada materia se creará un template que estarán dentro de la templates/inicio/materias: `Administracio.html`, `Contabilidad.html` y `Rrhh`.

29. **Configuración de material de estudio por asignatura:**
En cada uno de los templates dentro de `materias` se incorporará el material de estudio personalizado con hipervínculos que deriven hacia las presentaciones (en su mayoría) de plataforma Genial.ly. Se separan en secciones, tales como: presentaciones, videos explicativos, actividades lúdicas, trabajos prácticos integrativos, carpeta de trabajos prácticos (en el caso de materias prácticas como Contabilidad) y material adicional si lo amerita.

30. **Incorporación de "Sobre Mí":**
Para la incorporación del apartado "Sobre Mi", se procedió a crear una vista dentro de la aplicación inicio, una url y template `sobre_mi.html`, el cual contiene breve información sobre la trayectoria docente de la autora del sitio web, y su contacto de las diferentes redes sociales.

31 **Video explicativo del proyecto:**
Se realizó un video explicativo ([Link AQUÍ](https://www.youtube.com/watch?v=xt91jyZyDKE)) que resume la funcionalidad de cada sección del sitio web diseñado con Python a través de Django. Asimismo, a continuación se expone un gif que resume su contenido (puede demorar unos minútos en cargar por su peso):

<img align="right" alt="qr_wifly" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/Proyecto-de-Python-con-Django.gif"> &nbsp;<br>

___
<h2 align="center">¡Muchas gracias por su visita! <img src="https://github.com/ABSphreak/ABSphreak/blob/master/gifs/Hi.gif" width="30px"></h2>