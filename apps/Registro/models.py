from django.db import models

# Create your models here.
class Persona(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)
