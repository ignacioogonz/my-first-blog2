from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.CASCADE)

    
 


class Datos_Personales(models.Model):
    correo = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    telefono = models.CharField(max_length=50)
    #cosa = models.SelectMultiple(max_length=50)
    #opt = models.SelectMultiple(max_length=50)
    #Escriba = models.TextField()


class Datos(models.Model):
    correo = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    telefono = models.CharField(max_length=50)
    #cosa = models.SelectMultiple(max_length=50)
    #opt = models.SelectMultiple(max_length=50)
    #Escriba = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.rut

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email




