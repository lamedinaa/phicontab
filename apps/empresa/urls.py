from django.conf.urls import include, url
from apps.empresa.views import *


urlpatterns = [
    url(r'^inicio/$',inicio,name = "inicioUrls"),
    url(r'^puc/$',puc,name = "pucUrls"),
    url(r'^reportes/$',reportes,name = "reportesUrls"),
    url(r'^libro/$',libro,name = "libroUrls"),
    url(r'^inventarios/$',inventarios,name = "inventariosUrls"),
]
