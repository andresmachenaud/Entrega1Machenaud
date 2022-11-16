from django.db import models

# Create your models here.

class Libro(models.Model):

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    año = models.IntegerField()
    editorial = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
