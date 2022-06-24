from os import name
from django import views
from django.urls import path



from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('home.html',home,name="home"),
    path('home2.html',home2,name="home2"),
    path('home3.html',home3,name="home3"),
    path('contacto.html',contacto,name="contacto"),
    path('login.html',login,name="login"),
    path('Registro.html',Registro,name="Registro"),
    path('BandanaB.html',BandanaB,name="BandanaB"),
    path('BandanaF.html',BandanaF,name="BandanaF"),
    path('ArnesN.html',ArnesN,name="ArnesN"),
    path('ArnesF.html',ArnesF,name="ArnesF"),
    path('CollarP.html',CollarP,name="CollarP"),
    path('CollarH.html',CollarH,name="CollarH"),
    path('HuesoP.html',HuesoP,name="HuesoP"),
    path('HuesoPJ.html',HuesoPJ,name="HuesoPJ"),
    path('Registrar_usuario',registrar_persona),
    path('Registrar_contacto',registrar_contacto),
    path('Compra_usuario',registrar_compra),
    path('form-mod-contacto/<id>',form_mod_contacto, name="form_mod_contacto"),
    path('form-mod-registro/<id>',form_mod_registro, name="form_mod_registro"),
    path('form-mod-compra/<id>',form_mod_Compra, name="form"),
    path('Editar-contacto/',editar_contacto , name="Editar_contacto"),
    path ('Editar-registro/', editar_registro, name="Editar_registro"),
    path ('Consultar-datos',consultar_datos, name="Consultar_datos"),
    path ('Consultar-registro/', consultar_registro, name="Consultar_registro"),
    path ('consultarre-datos',consultarre_datos, name="consultarre_datos"),
    path ('consultarre-registro/', consultarre_registro, name="consultarre_registro"),
    path ('consultarcompra-datos',consultarcompra_datos, name="consultarcompra_datos"),
    path ('consultarcompra-registro/',consultarcompra_registro, name="consultarcompra_registro"),
    path ('Compra',Compra, name="Compra"),
    
    
]