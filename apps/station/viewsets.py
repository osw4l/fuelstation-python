from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from . import serializers
from . import models


class EstacioViewSet(viewsets.ModelViewSet):
    queryset = models.Estacion.objects.all()
    serializer_class = serializers.EstacionSerializer

    @detail_route(methods=['get'])
    def combustibles(self, request, pk=None):
        queryset = models.EstacionCombustible.objects.filter(estacion_id=pk)
        serializer = serializers.EstacionCombustibleSerializer(queryset, many=True)
        return Response({
            'combustibles': serializer.data
        })

