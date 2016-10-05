from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    email = models.EmailField(blank=False, null=False, max_length=100)
    contra = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return 'Perfil: {}'.format(self.nombre)

class datosExtra(models.Model):
    user = models.OneToOneField(User, blank=False)
    telefono = models.CharField(blank=True, max_length=100)
    direccion = models.CharField(blank=True, max_length=100)
