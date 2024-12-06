
from django.urls import path, include #camino e incluir
from registro.views import UsuarioCreateView
from registro.views import UsuarioListView
from django.contrib import admin


urlpatterns = [
    path('registro/', UsuarioCreateView.as_view(), name='registro'), # ruta para crear un usuario
    path('admin/', admin.site.urls),
    # esta es la ruta de la api 
    path('api/', include('registro.urls')),  
    path('usuarios/', UsuarioListView.as_view(), name='lista_usuarios'),  # Ruta para listar los usuarios
]

