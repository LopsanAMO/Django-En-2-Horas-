from django.contrib.auth.models import User
from .models import datosExtra

def guardarUser(datos):
	username=datos.get('nombre')
	password=datos.get('contra')
	email=datos.get('email')
	telefono=datos.get('telefono')
	direccion=datos.get('direccion')
	try:
		user = User.objects.create_user(username=username, password=password, email=email)
		user.save()
	except Exception as e:
		print(e)
		print(type(e))
	try:
		datos = datosExtra()
		datos.user = user
		datos.telefono = telefono
		datos.direccion = direccion
		datos.save()
	except Exception as e:
		print(e)
		print(type(e))