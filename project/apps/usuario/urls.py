from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', views.registrar_usuario, name='registro'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
]
    # Otras URLs del proyecto
   # Agrega esta línea para incluir las URLs de la aplicación "usuario"

