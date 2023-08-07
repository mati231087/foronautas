from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import RegistroForm

class RegistroUsuarioAdmin(UserAdmin):
    add_form = RegistroForm
    form = RegistroForm
    model = Usuario
    list_display = ['username', 'nombre_completo', 'correo_electronico']  # Personaliza las columnas que quieres mostrar en la lista de usuarios

admin.site.register(Usuario, RegistroUsuarioAdmin)

# Register your models here.
