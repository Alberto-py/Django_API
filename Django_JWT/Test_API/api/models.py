from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=150)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

opc_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opc_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre