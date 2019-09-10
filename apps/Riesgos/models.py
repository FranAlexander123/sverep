from django.db import models

# Create your models here.
class Riesgo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    justificacion = models.CharField(max_length=500)
    objetivo = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=700)

class Test(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    fecha = models.DateField(max_length=500)
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=1)
    diasLimite = models.IntegerField(max_length=700)
    diagnostico = models.CharField(max_length=100)


class Pregunta(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    respuesta = models.CharField(max_length=200)
    pregunta = models.CharField(max_length=200)

class SabiasQue(models.Model):
     id = models.CharField(primary_key=True, max_length=10)
     nombre = models.CharField(max_length=100)
     descripcion = models.CharField(max_length=500)
     demostracion = models.CharField(max_length=500)

class PosibleEnfermedad(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)