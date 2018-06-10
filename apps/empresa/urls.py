from django.conf.urls import include, url
from apps.empresa.views import *


urlpatterns = [
    url(r'^home/$',home,name = "HomeUrls"),
]
