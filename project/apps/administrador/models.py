from django.db import models

class Administrador(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def login(self, usuario, contraseña):
        if self.usuario == usuario and self.contraseña == contraseña:
            return True
        else:
            return False

