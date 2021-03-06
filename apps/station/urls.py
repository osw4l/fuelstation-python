from django.conf.urls import url, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'estaciones', viewsets.EstacionViewSet)

urlpatterns = [
    url(r'^viewsets/', include(router.urls))
]
