from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre=models.CharField (max_length=40) # charfield es tipo de dato (SQL) string y con largo max 40
    camada= models.IntegerField() #interger es tipo de dato entero

class Estudiante (models.Model):
    nombre=models.CharField (max_length=30) 
    apellido= models.CharField (max_length=30)
    email= models.EmailField()

class Profesor (models.Model):
    nombre=models.CharField (max_length=30) 
    apellido= models.CharField (max_length=30)
    email= models.EmailField()  # el tipo es especifico de email, cvalida que tenga @, punto etc.
    profesion= models.CharField (max_length=30)

class Entregable (models.Model):
    nombre=models.CharField (max_length=30) 
    fechaDeEntrega= models.DateField()
    entregado=models.BooleanField()
    