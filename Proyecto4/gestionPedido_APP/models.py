from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedido(models.Model):
    nropedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()



# python manage.py check gestionPedido_APP

# python manage.py makemigrations

# python manage.py migrate   

