from rest_framework import serializers
from registro.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario # este es el modelo al que corresponde el serializador
        fields = ['id', 'nombre', 'apellido', 'identificacion', 'fecha_nacimiento', 'correo', 'telefono', 'contraseña']
        #estos son los campos con los que se incluyen las respuestas
        extra_kwargs = {
            'contraseña': {'write_only': True}  # no se devuelve la contraseña en las respuestas.
        }
