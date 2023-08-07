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

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if not any(char.isupper() for char in password1) or not any(char.islower() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos una mayúscula y una minúscula.")
        password_validation.validate_password(password1, self.instance)
        return password1

    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('nombre_completo', 'fecha_nacimiento', 'correo_electronico', 'telefono', 'usuario')
