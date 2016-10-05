from django.contrib import admin
from .models import Usuario, datosExtra

@admin.register(Usuario)

class adminUsuario(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'contra')

@admin.register(datosExtra)

class adminDatos(admin.ModelAdmin):
	list_display = ('user', 'telefono', 'direccion')