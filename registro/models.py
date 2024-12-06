from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=100) #campo de caracteres y longitud maxima
    apellido = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True) #unica
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=100) 

    def __str__(self): # este define cómo se debe representar el objeto usuario como una cadena de texto.
        #y cuando el objeto Usuario se imprima se mostrará el nombre y el apellido completo del usuario.
        return f"{self.nombre} {self.apellido}"
