from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(max_length=255)
    fecha_nacimiento = forms.DateField()
    correo_electronico = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    usuario = forms.CharField(max_length=255)

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get("contraseña")
        if not any(char.isupper() for char in contraseña) or not any(char.islower() for char in contraseña):
            raise forms.ValidationError("La contraseña debe contener al menos una mayúscula y una minúscula.")
        password_validation.validate_password(self.cleaned_data.get("contraseña"), self.instance)
        return contraseña

    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'fecha_nacimiento', 'correo_electronico', 'telefono', 'usuario', 'contraseña']
