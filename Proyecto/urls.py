from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blogUrl

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(blogUrl, namespace='user'))
]
