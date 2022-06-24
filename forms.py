from django import forms
from django.forms import ModelForm
from .models import  Registroo
from .models import Contacto
from .models import Comprar



class RegistroForm(ModelForm):
    class Meta:
        model = Registroo
        fields =['Nombre','Rut','Edad','Email','Telefono','Contraseña']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields =['Nombre', 'Rut','Apellido', 'Email', 'Asunto','Asunto2']

class ComprarForm(ModelForm):
    class Meta:
        model = Comprar
        fields =['Producto', 'Cantidad','Tipotarjeta', 'Numerotarjeta', 'Fecha_expira','Cvv','Direccion']


