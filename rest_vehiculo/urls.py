
from django.urls import path
from rest_vehiculo.views import lista_comprar,lista_contacto,lista_registro,detalle_comprar

urlpatterns = [
    path('lista_registro/', lista_registro, name="lista_registro"),
    path('lista_contacto/', lista_contacto, name="lista_contacto"),
    path('lista_comprar/', lista_comprar, name="lista_comprar"),
    path('detalle_comprar/<id>', detalle_comprar, name="detalle_comprar"),
   
    
]
