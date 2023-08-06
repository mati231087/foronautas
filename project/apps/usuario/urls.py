from django.contrib import admin
from django.urls import path, include

app_name = 'usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Otras URLs del proyecto
   # Agrega esta línea para incluir las URLs de la aplicación "usuario"
]
