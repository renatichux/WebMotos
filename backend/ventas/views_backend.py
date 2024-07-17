# RestFull Basado en Clases
# https://www.django-rest-framework.org/tutorial/3-class-based-views/

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
#from .models import Region,Persona,Comuna
from .models import *
#from .serializers import RegionSerializer,PersonaSerializer
from .serializers import *

# Create your views here.

def indexHarrys(request):
    return HttpResponse("Harrisito El Magnifico, Doble Magnifico")

class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)


class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg,**kwargs):
        #print("data",data)
        data= {"OK":True,"count":"1","registro":data,"msg":msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, **kwargs):
        data= {"OK":False,"count":"0","msg":data}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)



class SucursalList(APIView):
    def get(self, request, format=None):
         registro = Sucursal.objects.all()
         serializer = SucursalSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = SucursalSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)

class SucursalList(APIView):
    def get_object(self, pk):
        try:
            return Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = SucursalSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = SucursalSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GeneroList(APIView):
    def get(self, request, format=None):
         registro = Genero.objects.all()
         serializer = GeneroSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

class RegionList(APIView):
    def get(self, request, format=None):
         registro = Region.objects.all()
         serializer = RegionSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class ProvinciaList(APIView):
    def get(self, request,region, format=None):
         #registro = Provincia.objects.all()
         #registro = Provincia.objects.get(region=region) #para Obtener un registro
         registro = Provincia.objects.filter(region=region) # Filtrar por un campo
         serializer = ProvinciaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
    
class ComunaList(APIView):
    def get(self, request,provincia, format=None):
         #registro = Comuna.objects.all()
         registro = Comuna.objects.filter(provincia=provincia) # Filtrar por un campo
         serializer = ComunaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")

class PersonaList(APIView):
    def get(self, request, format=None):
         registro = Persona.objects.all()
         serializer = PersonaSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")
         #return Response(serializer.data)

    def post(self, request, format=None):
        #print("1,Post",request)
        # insert en la tabla cliente
        # insert en la tabla usuario
        data = JSONParser().parse(request)
        #print("1",data)
        registro = PersonaSerializer(data=data)
        #print("2",registro)
        if registro.is_valid():
            #print("3")
            # Enviar harrys
            registro.save()
            #print("4")
            return JSONResponseOk(registro.data, status=status.HTTP_201_CREATED,msg="")
        #return JSONResponseErr(registro.errors, status=status.HTTP_400_BAD_REQUEST)
        # Envimaos como Okey el Http, pero con mensaje de Error
        return JSONResponseErr(registro.errors, status=status.HTTP_201_CREATED)
    
class PersonaDetail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        #print("Persona Rut",pk)
        registro = self.get_object(pk)
        #print("Registro Rut",registro)
        serializer = PersonaSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")

    def put(self, request, pk, format=None):
        #print("put.1**",request)
        registro = self.get_object(pk)
        #print("put.2**",registro)
        data = JSONParser().parse(request)
        #print("put.3**",data)
        serializer = PersonaSerializer(registro, data=data)
        if serializer.is_valid():
            serializer.save()
            #return JSONResponseOk(serializer.data)
            return JSONResponseOk(None,msg="Resistro Actualizado")
        return JSONResponseErr(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        registro = self.get_object(pk)
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

#################      CON NEGOCIO, más ordenado
from rest_framework.permissions import IsAuthenticated
from .negocio import *
class ClienteList(APIView):
    #permission_classes = (IsAuthenticated,)
#### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['papellido'],data['sapellido']
                            ,data['email']
                            ,data['comuna'],data['genero'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Resistro Actualizado")
from django.http import JsonResponse    
class ClienteDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request, rut, format=None):
        registro = Negocio.clienteGet(rut)
        serializer = ViewClienteSerializer(registro)
        #print("Registro serializer",serializer)
        return JSONResponseOk(serializer.data,msg="")
    
#### Observe que  clienteCrear se llama dos veces en el post y en el Put
    def put(self, request,rut, format=None):
        data = JSONParser().parse(request)
        if (not Negocio.clienteCrear(data['rut'],data['dv']
                            ,data['nombre'],data['papellido'],data['sapellido']
                            ,data['email']
                            ,data['comuna'],data['genero'])):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponseOk(None,msg="Resistro Actualizado")

    def delete(self, request, rut, format=None):
        if (not Negocio.clienteEliminar(rut)):
            return JSONResponseErr(None, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
# from rest_framework_simplejwt.tokens import RefreshToken

# class LoginView(APIView):
#     def post(self, request):
#         # Perform authentication checks here

#         # Generate tokens
#         refresh = RefreshToken.for_user("user")
#         access_token = str(refresh.access_token)

#         return Response({'access_token1': access_token})

class ProductosList(APIView):
    def get(self, request, format=None):
         registro = Productos.objects.all()
         serializer = ViewProductosSerializer(registro, many=True)
         return JSONResponseOkRows(serializer.data,"")