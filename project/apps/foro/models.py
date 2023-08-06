from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(max_length=30000)
    imagen = models.ImageField(upload_to='temas/', null=True, blank=True)
    video = models.FileField(upload_to='temas/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    contenido = models.TextField(max_length=30000)
    imagen = models.ImageField(upload_to='comentarios/', null=True, blank=True)
    video = models.FileField(upload_to='comentarios/', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido


# Create your models here.
