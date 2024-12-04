from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido', 'identificacion', 'fecha_nacimiento', 'correo', 'telefono', 'contraseña']
        extra_kwargs = {
            'contraseña': {'write_only': True}  # No devolver la contraseña en las respuestas.
        }
