from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    usuario = models.CharField(max_length=255, unique=True)
    contraseña = models.CharField(max_length=255)  # Se puede agregar validaciones adicionales para la contraseña

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuario_user'  # Agrega el related_name único para evitar conflictos
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuario_user'  # Agrega el related_name único para evitar conflictos
    )

    def __str__(self):
        return self.usuario


# Create your models here.
