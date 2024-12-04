from django.urls import path
from .views import UsuarioCreateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('registro/', UsuarioCreateView.as_view(), name='registro'),
    path('admin/', admin.site.urls),
    path('api/', include('registro.urls')),  # Ruta para la API
]

