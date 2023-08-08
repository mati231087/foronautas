from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Tema, Comentario
from .forms import TemaForm, ComentarioForm

def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST, request.FILES)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.usuario = request.user
            tema.save()
            return redirect('detalle_tema', tema_id=tema.id)
    else:
        form = TemaForm()
    return render(request, 'crear_tema.html', {'form': form})

def editar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id, usuario=request.user)
    if request.method == 'POST':
        form = TemaForm(request.POST, request.FILES, instance=tema)
        if form.is_valid():
            form.save()
            return redirect('detalle_tema', tema_id=tema.id)
    else:
        form = TemaForm(instance=tema)
    return render(request, 'editar_tema.html', {'form': form, 'tema': tema})

def eliminar_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id, usuario=request.user)
    tema.delete()
    return redirect('lista_temas')

def detalle_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    comentarios = tema.comentario_set.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.tema = tema
            comentario.save()
            return redirect('detalle_tema', tema_id=tema.id)
    else:
        form = ComentarioForm()
    return render(request, 'detalle_tema.html', {'tema': tema, 'comentarios': comentarios, 'form': form})

def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id, usuario=request.user)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('detalle_tema', tema_id=comentario.tema.id)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'editar_comentario.html', {'form': form, 'comentario': comentario})

def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id, usuario=request.user)
    comentario.delete()
    return redirect('detalle_tema', tema_id=comentario.tema.id)

def obtener_temas(request):
    temas = Tema.objects.all()
    temas_json = []
    for tema in temas:
        temas_json.append({
            'titulo': tema.titulo,
            'contenido': tema.contenido
        })
    return JsonResponse({'temas':temas_json})


# Create your views here.
