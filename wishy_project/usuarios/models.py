from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(AbstractUser):
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'usuarios_usuarios'