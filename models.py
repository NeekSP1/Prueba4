from django.db import models

# Create your models here.

class Registroo(models.Model): 
    Nombre = models.CharField(max_length=6,  verbose_name='Nombre')
    Rut = models.CharField(max_length=9,primary_key=True,  verbose_name='Rut')
    Edad = models.CharField(max_length=2, verbose_name='Edad')
    Email = models.CharField(max_length=20,  verbose_name='E-mail')
    Telefono = models.CharField(max_length=9, verbose_name='Telefono')
    Contraseña = models.CharField(max_length=20,  verbose_name='Contraseña')
    
    def __int__(self):
        return self.Rut




class Contacto(models.Model):   
    Nombre = models.CharField(max_length=10, verbose_name='Nombre')
    Rut = models.CharField(max_length=9,primary_key=True,  verbose_name='Rut')
    Apellido = models.CharField(max_length=10, verbose_name='Apellido')
    Email = models.CharField(max_length=20,  verbose_name='E-mail')
    Asunto = models.CharField(max_length=9, verbose_name='Asunto')
    Asunto2 = models.CharField(max_length=20,  verbose_name='Asunto2')
    
    def __int__(self):
        return self.Rut

class Comprar(models.Model):
    Producto = models.CharField(max_length=100, verbose_name='Producto')
    Cantidad = models.CharField(max_length=100, verbose_name='Cantidad')
    Tipotarjeta = models.CharField(max_length=100, verbose_name='Tipotarjeta')
    Numerotarjeta=models.CharField(max_length=100,primary_key=True,verbose_name='Numerotarjeta')
    Fecha_expira=models.CharField(max_length=100, verbose_name='Fecha_expira')
    Cvv=models.CharField(max_length=100,verbose_name='CVV')
    Direccion=models.CharField(max_length=100,verbose_name='Direccion')

    def __int__(self):
        return self.Numerotarjeta

class Producto(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    Stock = models.CharField(max_length=100, verbose_name='Stock')
    Precio = models.CharField(max_length=100, verbose_name='Precio')

    def __int__(self):
        return self.Nombre 
