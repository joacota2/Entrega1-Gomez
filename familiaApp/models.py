from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    numero=models.IntegerField()
    nacimiento=models.DateField()


    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    




