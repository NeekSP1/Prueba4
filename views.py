import email
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render 
from .models import *
from .forms import *




# Create your views here.

def home(request):

    return render(request, 'core/home.html')
    

def home2(request):

    return render(request, 'core/home2.html')

def home3(request):
    datos={

    }
    todos=Producto.objects.all()
    datos['Stock']=todos

    return render(request, 'core/home3.html')

def contacto(request):

    return render(request, 'core/contacto.html')

def login(request):

    return render(request, 'core/login.html')

def Registro(request):
   

    return render(request, 'core/Registro.html')

def BandanaB(request):
    datos={

    }
    todos=Producto.objects.all()
    datos['Stock']=todos


    return render(request, 'core/BandanaB.html')

def BandanaF(request):
  
    return render(request, 'core/BandanaF.html')

def ArnesN(request):

    return render(request, 'core/ArnesN.html')

def ArnesF(request):

    return render(request, 'core/ArnesF.html')

def CollarP(request):

    return render(request, 'core/CollarP.html')

def CollarH(request):

    return render(request, 'core/CollarH.html')


def HuesoP(request):

    return render(request, 'core/HuesoP.html')

def HuesoPJ(request):
  

    return render(request, 'core/HuesoPJ.html')



def consultar_datos(request):
    
    return render (request, 'core/Consultar-datos.html')

def consultarre_datos(request):
    
    return render (request, 'core/consultarre-datos.html')

def consultarcompra_datos(request):
    
    return render (request, 'core/consultarcompra-datos.html')


def Compra(request):

    

    return render(request, 'core/Compra.html')



#Registarando en la base de datos ------------------------------------------------------------------------------------------------------------
def registrar_persona(request):
    datos={

    }
    Nombre=request.POST['Nombre']
    Rut=request.POST['Rut']
    Edad=request.POST['Edad']
    Email=request.POST['Email']
    Telefono=request.POST['Telefono']
    Contraseña=request.POST['Contraseña']
    
    datos['mensaje']= "Registro completado"
    codigo=Registroo.objects.create(Nombre=Nombre,Rut=Rut,Edad=Edad,Email=Email,Telefono=Telefono,Contraseña=Contraseña)
    return render(request, 'core/Registro_completo.html')
    

def registrar_contacto(request):
    Nombre=request.POST['Nombre']
    Rut=request.POST['Rut']
    Apellido=request.POST['Apellido']
    Email=request.POST['Email']
    Asunto=request.POST['Asunto']
    Asunto2=request.POST['Asunto2']
    
    codigo=Contacto.objects.create(Nombre=Nombre,Rut=Rut, Apellido=Apellido,Email=Email,Asunto=Asunto,Asunto2=Asunto2)
    return render(request,'core/contacto.html')

def registrar_compra(request):
    datos={

    }
    Producto=request.POST['Producto']
    Cantidad=request.POST['Cantidad']
    Tipotarjeta=request.POST['Tipotarjeta']
    Numerotarjeta=request.POST['Numerotarjeta']
    Fecha_expira=request.POST['Fecha_expira']
    Cvv=request.POST['Cvv']
    Direccion=request.POST['Direccion']
    
    datos['mensaje']= "Registro completado"
    codigo=Comprar.objects.create(Producto=Producto,Cantidad=Cantidad,Tipotarjeta=Tipotarjeta,Numerotarjeta=Numerotarjeta,Fecha_expira=Fecha_expira,Cvv=Cvv,Direccion=Direccion)
    return render(request, 'core/Compra_completo.html')
    
#----------------------------------------------------------------------------------------------------------------------------------------------

#def form_mod_contacto(request, id):
    contacto = Contacto.objects.get(Nombre=id)
    datos ={
        'form': ContactoForm(instance=contacto)
    }
    if request.method=='POST':
        formulario = ContactoForm(data = request.POST, instance=contacto)
        if formulario.is_valid: 
            formulario.save()
            return redirect('home')
    return render(request, 'core/form_mod_contacto.html', datos)

def consultar_registro(request):
    datos={

    }
    Rut=request.POST['Nombre']
    codigo=Contacto.objects.filter(Rut=Rut)

    if codigo:
        datos['mensaje']= "Usuario encontrado correctamente"
        Contactox=Contacto.objects.get(Rut=Rut)
        datos['Contacto']=Contactox
        return render (request, 'core/Consultar-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/Consultar-registro.html',datos)

def consultarre_registro(request):
    datos={

    }
    Rut=request.POST['Nombre']
    codigo=Registroo.objects.filter(Rut=Rut)

    if codigo:
        datos['mensaje']= "Usuario encontrado correctamente"
        Registroox=Registroo.objects.get(Rut=Rut)
        datos['Registroo']=Registroox
        return render (request, 'core/consultarre-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/consultarre-registro.html',datos)

def consultarcompra_registro(request):
    datos={

    }
    Numerotarjeta=request.POST['Numerotarjeta']
    codigo=Comprar.objects.filter(Numerotarjeta=Numerotarjeta)

    if codigo:
        datos['mensaje']= "Usuario encontrado correctamente"
        Comprarx=Comprar.objects.get(Numerotarjeta=Numerotarjeta)
        datos['Comprar']=Comprarx
        return render (request, 'core/consultarcompra-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/consultarcompra-registro.html',datos)








   
def form_mod_contacto(request,id):
    persona= Contacto.objects.get(Rut=id)

    datos= {
        'form': ContactoForm(instance=persona),
        'Contacto':persona
        
    }
    return render(request, 'core/form_mod_contacto.html',datos)


def form_mod_registro(request,id):
    persona= Registroo.objects.get(Rut=id)

    datos= {
        'form': RegistroForm(instance=persona),
        'Persona':persona
        
    }
    return render(request, 'core/form_mod_registro.html',datos)


def form_mod_Compra(request,id):
    persona= Comprar.objects.get(Numerotarjeta=id)

    datos= {
        'form': ComprarForm(instance=persona),
        'Persona':persona
        
    }
    return render(request, 'core/form_mod_compra.html',datos)




def editar_registro(request):
    Nombre=request.POST['Nombre']
    Rut=request.POST['Rut']
    Edad=request.POST['Edad']
    Email=request.POST['Email']
    Telefono=request.POST['Telefono']
    Contraseña=request.POST['Contraseña']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"
    persona= Registroo.objects.get(Rut=Rut)
    persona.Nombre=Nombre
    persona.Edad=Edad
    persona.Email=Email
    persona.Telefono=Telefono
    persona.Contraseña=Contraseña
    persona.save()

    return redirect('/')

def editar_contacto(request):
    
    Nombre=request.POST['Nombre']
    Rut=request.POST['Rut']
    Apellido=request.POST['Apellido']
    Email=request.POST['Email']
    Asunto=request.POST['Asunto']
    Asunto2=request.POST['Asunto2']

    codigo=Contacto.objects.get(Rut=Rut)
    codigo.Nombre=Nombre
    codigo.Apellido=Apellido
    codigo.Email=Email
    codigo.Asunto=Asunto
    codigo.Asunto2=Asunto2
    codigo.save()
    return redirect('/')


