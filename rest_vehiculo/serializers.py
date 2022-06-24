from rest_framework import serializers
from core.models import Contacto,Registroo,Comprar

class RegistrooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registroo
        fields =['Nombre','Rut','Edad','Email','Telefono','Contraseña']

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields =['Nombre', 'Rut','Apellido', 'Email', 'Asunto','Asunto2']

class ComprarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprar
        fields =['Producto', 'Cantidad','Tipotarjeta', 'Numerotarjeta', 'Fecha_expira','Cvv','Direccion']

