from django.shortcuts import render
from .models import Administrador

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        administrador = Administrador.objects.first()  # Obtener el primer administrador (puedes ajustar esta lógica según tus necesidades)
        if administrador.login(usuario, contraseña):
            # Lógica para autenticación exitosa
            return render(request, 'administrador/login_success.html')
        else:
            # Lógica para autenticación fallida
            return render(request, 'administrador/login_fail.html')
    else:
        # Lógica para renderizar el formulario de login
        return render(request, 'administrador/login.html')

#
