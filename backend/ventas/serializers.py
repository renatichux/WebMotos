from rest_framework import serializers
from .models import *


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('idSucursal','codigo', 'nombre','comuna','direccion','fCreacion')





class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('idGenero','codigo', 'nombre')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('idRegion','codigo', 'nombre')

class RegionSerializerPutDelRead(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codigo', 'nombre')        

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idProvincia','codigo', 'nombre','region')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('idComuna','codigo', 'nombre','provincia')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('rut', 'dv', 'fechaNacimiento', 'nombre', 'papellido', 'sapellido', 'email','comuna','genero')

class ViewClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewCliente
        fields = ('rut', 'dv',  'nombre', 'papellido', 'sapellido', 'email','comuna','genero')

class ViewProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('idProd','imagen','imagen_sb','nombre','desc_corta','cant_favoritos','cant_vistos','precio')


