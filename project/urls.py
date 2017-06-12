"""guard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from .settings import base
from django.contrib import admin
from apps.main.views import log_in as entrar, salir
from apps.utils import errors

urlpatterns = [

    #frameworks y plugins
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),

    # administrar sesiones
    url(r'^$', entrar, name='entrar'),
    url(r'^api/', include('apps.station.urls')),
    url(r'^salir/', salir, name='salir'),

] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)


handler400 = errors.error400
handler403 = errors.error403
handler404 = errors.error404
handler500 = errors.error500
