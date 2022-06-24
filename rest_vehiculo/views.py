from django.shortcuts import render
from ast import If
from asyncio.windows_events import NULL
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Comprar,Contacto,Registroo
from .serializers import RegistrooSerializer, ContactoSerializer, ComprarSerializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_registro(request):
    """
    Lista de todos las personas registradas
    """
    if request.method == 'GET':
        persona = Registroo.objects.all()
        serializer = RegistrooSerializer(persona, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = RegistrooSerializer(data=request.data)
        rut=request.POST['rut']
        personaencontrada=Registroo.objects.filter(rut=rut)
        datos={

        }
        if serializer.is_valid():
            if personaencontrada:
                datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
                return render(request, 'core/Registro_resultado.html',datos)
            else:
                datos['mensaje']= "Registro completado"
                serializer.save()
                return render(request, 'core/Registro_resultado.html',datos)
        else:
            datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
            return render(request, 'core/Registro_resultado.html',datos)


@csrf_exempt
@api_view(['GET','POST'])
def lista_contacto(request):
    """
    Lista de todos los contactos de la pagina
    """
    if request.method == 'GET':
        contacto = Contacto.objects.all()
        serializer = ContactoSerializer(contacto, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ContactoSerializer(data=request.data)
        datos ={

        }
        if serializer.is_valid():
            serializer.save()
            datos['mensaje']= "Contacto completada"
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            datos['mensaje']= "Se ha producido un error inesperado, el contacto no se pudo efectuar"
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@csrf_exempt
@api_view(['GET','POST'])
def lista_comprar(request):
    """
    Lista de todos las Compra
    """
    if request.method == 'GET':
        Compra = Comprar.objects.all()
        serializer = ComprarSerializer(Compra, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ComprarSerializer(data=request.data)
        datos ={

        }
        if serializer.is_valid():
            serializer.save()
            datos['mensaje']= "Compra completada"
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            datos['mensaje']= "Se ha producido un error inesperado, la compra no se pudo efectuar"
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE','POST'])
def detalle_comprar(request,id):
    """
    Get, Update, o delete de una persona en particular
    """
    persona = Comprar.objects.get(Numerotarjeta=id)
    try:
        persona = Comprar.objects.get(Numerotarjeta=id)
    except Comprar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ComprarSerializer(persona)
        return Response(serializer.data)
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ComprarSerializer(persona, data=request.data)
        if serializer.is_valid():
            datos={
            }
            datos['mensaje'] = "Modificados correctamente"
            serializer.save()
            return render(request, 'api/lista_comprar',datos)
       
    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











