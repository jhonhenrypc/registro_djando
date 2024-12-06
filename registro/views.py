from django.shortcuts import render


from rest_framework import generics
from registro.models import Usuario
from registro.serializers import UsuarioSerializer

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all() #esta línea especifica los datos con los que esta vista va a trabajar
    serializer_class = UsuarioSerializer #este especifica qué clase de serializador se va a utilizar 
    #para convertir el modelo de datos usuario a un formato que pueda ser enviado como respuesta HTTP

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all() #lo mismo con esta
    serializer_class = UsuarioSerializer

