from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    institucion = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido} | {self.email} | {self.institucion} | {self.materia}"