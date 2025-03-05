## Proyecto de Página Web a través de Python con Django

<img align="right" alt="Python" width="250" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/python.gif">

El presente proyecto se basa en la creación de un sitio web basado en Python con la implementación del firmware Django, a través del editor Visual Studio Code.
Se espera que a través del sitio web se puedan ingresar datos por medio de un formulario, listar esos datos, y buscar datos dentro de la base de datos creada anteriormente con un formulario.

1. **Configuración Inicial de Git y GitHub:**
Inicialmente se realiza la conexión y configuración de git al repositorio con los comandos correspondientes, antes de ello se recomienda configurar (y en caso que ya esté hecho) corroborar los datos de esa configuración global guardados en la carpeta de usuario
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
Se puede manejar estos mismos movimientos desde interface gráfica, pero en el caso del presente proyecto fue gestionado 100% desde terminal. Se recomienda instalar la extensión `GitGraph` para observar el historial del cambios que fueron efectuados en la rama correspondiente desde el mismo Visual Studio Code.
Es importante, posicionarse en la "rama" adecuada en la que se desea trabajar en el repositorio, para evitar conflictos y versiones distintas en diferentes ubicaciones. La más común es main, y el posicionamiento en la misma se efectúa con el comando `git checkout main`, para ver todas las ramas `git branch` y para crear una nueva rama `git checkout -b nombre-de-la-rama`.

2. **Configuración del Gitignore:**
Antes de proceder a crear un entorno virtual que es recomendable para trabajar con django, será importante configurar el archivo .gitignore para evitar pushear cambios al repositorio que no deseamos o no es recomendable que sean visibles públicamente. Para ello, de un modo agilizado se recurre al sitio web `gitignore.io` seleccionando en este caso partícular "Visual Studio Code", "Python" y "Django".

3. **Creación y uso de un entorno virtual:**
En este tipo de proyectos se recomienda la creación de un entorno virtual en el cual se instalen y manejen solo las dependencias o paquetes específicos que requiere el proyecto y no todos los paquetes globales instalados localmente. A continuación se detallan los comandos para su creación y activación:
```
python -m venv venv # Creación de un entorno virtual, tener en cuenta que ese nombre debe coincidir con lo que figura en gitignore para evitar que se suba al repositorio
source venv/bin/actívate # Activación del entorno virtual
```

4. **Instalación de Django:**

<img align="right" alt="Django" width="80" src="https://github.com/JessBasile/TuPrimeraPagina-Basile/raw/main/imagenes/django-python-logo.png">

Se recomienda activar el entorno virtual y proceder a instalar django para hacerlo dentro del entorno.
```
pip install django # Para instalarse Django en el entorno virtual
pip freeze # Para observar los paquetes que tiene instalado el entorno (para ello ya debe estar activado el mismo)
```
Cada vez que se abra el proyecto en Visual Studio Code, se deberá activar el entorno virtual para que los cambios impacten adecuadamente en el proyecto.

5. **Creación y configuración del archivo requirements.txt:**
El archivo requirements.txt es necesario para listar todas las dependencias que el proyecto necesita y se configura con el siguiente comando:
```
pip freeze > requirements.txt
```
En el presente proyecto los paquetes recomendables son los siguientes:
```
asgiref==3.8.1
Django==5.1.6
sqlparse==0.5.3
tzdata==2025.1
```
En el caso que otro usuario descargue el proyecto, deberá crear su propio entorno local y ejecutar el comando `pip install -r requirements.txt` para instalar los paquetes que se necesitan en el nuevo entorno creado.

6. **Inicialización del Proyecto con Django:**
Se procede a iniciar el proyecto con Django ejecutando un comando que permite la creación de la estructura básica del proyecto con una carpeta (en este caso proyectoDjango), se crearán archivos clave como `manage.py` y `settings.py`.
```
django-admin startproject proyectoDjango .
```
El `.` al final colabora para que el archivo `manage.py` se crea en la carpeta raíz del proyecto, y además, la carpeta proyectoDjango con su `settings.py` dentro (que contiene las configuraciones por defecto de nuestro proyecto).

7. **Iniciar Servidor de desarrollo de Django con Python:**
El proyecto utilizará diferentes `URLs` para acceder a distintas `vistas` a través del navegador. Las vistas se encargan de la lógica de la aplicación, interactuando con los `modelos` (que representan la estructura de la base de datos) y los `templates` (archivos HTML que muestran la información al usuario).
Para poder crear esos archivos para cumplir las distintas finalidades, primero se deberá iniciar el servidor de desarrollo Django - generalmente - en la dirección `http://127.0.0.1:8000/` con la ejecución del siguiente comando:
```
python manage.py migrate
```
La primera vez que ejecuta ese comando, Django crea automáticamente una base de datos SQLite (`db.sqlite3`) con la aplicación de migraciones que aseguran la estructura de la base. El archivo deberá estar "oculto" por encontrarse mencionado dentro del archivo .gitignore. En ejecuciones posteriores, no se crea una nueva base de datos, sino que el servidor simplemente utiliza la existente.
Cada vez que se procedan a realizar modificaciones se deberá activar el entorno virtual y posteriormente correr el servidor para poder ir guardando los cambios del proyecto adecuadamente. El siguiente comando hará correr el servidor Django:
```
python manage.py runserver
```

8. **Creación de una vista en una aplicación:**
Dentro del archivo urls.py se crea una aplicación con el siguiente comando:
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
Para que se pueda acceder a la vista será necesario establecer path en el archivo urls.py dentro de la carpeta inicio, para ello, primero se deberá configurar en el archivo urls.py importando path:
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
Para crear templates se procede a crear una carpeta en la raiz general y otra carpeta igual pero dentro de inicio. La carpeta de templates (dentro de inicio), contendrá en su interior, otra carpeta llamada inicio, y allí se alojarán todos los .html de esa aplicación específica.
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
Se proceden a crear otras vistas dentro de la misma aplicación para lo cual se tendrán que realizar los mismos pasos efectuados anteriormente para la primera vista (iniciao). Por lo tanto, se configurará cada una de las nuevas vistas dentro de views.py con su nuevo nombre (tal como se hizo con inicio), crear un template dentro de templates/inicio con el mismo nombre que la vista .html y definir la url dentro del archivo urls.py importando y agregando su path.
En una de las vistas creadas en el presente proyecto se utilizaron diccionarios o contextos que se le pasaron al template para que cargue correctamente cierta información como puede ser hora y fecha actual con `datetime.now()` o un formulario con `{formulario}`.

11. **Incorporación de navegación en los templates:**
En cada archivo .html se debe configurar un menú de navegación con hipervínculos, permitiendo el acceso a las distintas páginas del proyecto. Esto se logra utilizando la etiqueta <nav> y la función url de Django para generar las rutas dinámicamente a través del nombre que se les asignó. Ejemplo del código a continuación:
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
La creación de los modelos son similar a las clases que contendrá atributos en los distintos campos (al igual que el caso de los formularios). Luego de su elaboración, se deberá "conectar" con la base de datos mediante el siguiente comando en terminal:
```
python manage.py makemigrations
```
De ese modo, se crea un archivo intermedio dentro de la carpeta migrations en la carpeta de la aplicación denominado `0001_initial.py` y tendrá número ascendente por cada cambio que se migre. De todos modos, los cambios no se encuentran impactados todavía en la base y para ello se ejecutará el comando migrate que trasladará esas migraciones:
```
python manage.py migrate
```
Se podrán corroborar las migraciones en el archivo db.sqlite3.

`Aclaración Importante:` Para que la ejecución del comando sea exitosa y se migre a la base de datos será necesario que la aplicación se encuentre configurada en el archivo settings.py de la carpeta proyectoDjango y que figure en los `INSTALLED_APP`, caso contrario no detectará los cambios.

13. **Elaboración de formularios en las distintas vistas:**
Los formularios se implementan a través de los templates de cada vista y estarán basados en el modelo de la aplicación. Sin embargo, es recomendable crear un archivo `forms.py` dentro de la aplicación, donde se definan los diferentes formularios que se utilizarán en las distintas vistas correspondientes.
Si cada aplicación dentro del proyecto requiere formularios, lo ideal es que cada una tenga su propio archivo forms.py para organizar y mantener el código de manera más estructurada.
Para el caso del formulario para inserción de datos es bajo método `POST` con la siguiente estructura de cración en html:
```
<form action="" method="POST">
```
Es utilizado para enviar datos al servidor y guardarlos en la base.
Los datos no son visibles en la URL. Éste método también podrá ser utilizado para modificación y eliminación de datos.
Para el caso de formulario destinado a consultas de los datos, no se especifica el método, y por lo tanto, es `GET` cuya finalidad es consulta o filtrado de datos.
En el archivo views.py en la siguiente línea de configuración sobre el comportamiento de los datos proporcionados a través del formulario, se verifica que todos los campos cumplen con las caracteristicas especificadas en forms.py:
```
if formulario.is_valid():
```
Y en la sección cleaned_data extrae los datos validados del formulario.
Por último, los templates que contienen formularios con condicionales utilizan `{& if %}`, `{% else %}`, `{% for %}`, etc.

14. **Herencia de templates:**
Para evitar la repetición de código en los templates, se implementa la herencia de templates y se recurre a utilizar un bootstrap de la página https://startbootstrap.com/ cuya estructura html se copia en un template denominado `template_base.html` dentro de la carpeta templates en la carpeta proyectoDjango y dentro de inicio se "extraen" los archivos que esa plantilla elegida de bootstrap contiene dentro de una carpeta denominada `static` (en la carpeta de la aplicación inicio).
Una vez creado el template base, se procederá a borrar en cada template de la aplicación inicio el código que se repite en todas, dejando solo el contenido específico de cada página/template. Asimismo, se incroporará al inicio de cada template la siguiente primera línea de código que "importará" el contenido base del template general:
```
{% extends "template_base.html" %}
```
Para que funcione exitosamente se incorpora un `block` en el template_base (antes que termine todo el HTML) para indicar que se incorporará contenido en otros templates, con el siguiente código:
```
    {% block contenido %}
    {% endblock contenido %}
```

15. **Creación de Formularios con ModelForm:**
Para permitir la edición de registros, se acrea un formulario en forms.py utilizando `ModelForm` con una sub-clase dentro `Meta`, que permitirá efectuar modificaciones y otro tipo de acciones sobre los registros.
Luego se incorporan tres vistas (con sus correspondientes urls) para poder eliminar registros, ver registros/consultarlos y modificar ese registro. Asimismo, en listado_de_alumos.html se deberá incorporar los links que deriven a las urls con interactividad que ejecuten esa acción ya sea eliminar, modificar o solo consultar.
Para el caso específico de modificar el registro, se creará una nueva clase dentro de forms.py `"ModificarAlumno"` con forms.ModelForm y Meta que permitirá identificar cierta configuración de la cual se puede especificar un modelo "Alumno" que lo deberé importar con:
```
from inicio.models import Alumno
```

16. **Clases basadas en vistas (CBV):**
Cuando se realizan clases basadas en vistas, se crea una nueva carpeta para colocar las clases basadas en vistas `CBV` dentro de la carpetas de templates ---> inicio.  Dentro del archivo views.py se deberá primero importar: 
```
from django.views.generic.edit import UpdateView 
```
Para utilizar un tipo de clase que nos proporciona Django UpdateView y también se deberá importar:
```
from django.urls import reverse_lazy
```
Esta última, es una funcionalidad que permite hacer lo mismo que el redirect pero para un `success_url`. Por último, en el archivo modificar_alumno.html se debe reemplazar `{{form}}` en donde se utiliza {{formulario}} para que lo tome adecuadamente y en el PATH en urls:
``` 
path('modificar-alumno/<int:pk>', ModificarAlumnoVista.as_view(), name='modificar_alumno'),
```
En el caso del eliminado, se efectúan los mismos pasos solo que en lugar de importar UpdateView en django.views se importará `DeleteView`. **Para eliminar en el caso de CBV será necesario un template porque requerirá CONFIRMAR**.

17. **