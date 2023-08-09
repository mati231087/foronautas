from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'base.html')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('nombre_de_la_ruta')  # Reemplaza 'nombre_de_la_ruta' con la ruta deseada después del inicio de sesión
    else:
        form = LoginForm()
    return render(request, 'usuario/iniciar-sesion.html', {'form': form})


# Create your views here.
