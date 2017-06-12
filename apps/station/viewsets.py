from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from . import serializers
from . import models


class EstacionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Estacion.objects.all()
    serializer_class = serializers.EstacionSerializer
    model = models.Estacion

    def get_queryset(self):
        return self.model.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response({
            'estaciones': serializer.data
        })

    @detail_route(methods=['get'])
    def combustibles(self, request, pk=None):
        queryset = models.EstacionCombustible.objects.filter(estacion_id=pk)
        serializer = serializers.EstacionCombustibleSerializer(queryset, many=True)
        return Response({
            'combustibles': serializer.data
        })

