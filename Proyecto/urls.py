from django.conf.urls import url, include
from django.contrib import admin
from usuario import urls as usuarioUrl

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(usuarioUrl, namespace='user'))
]
