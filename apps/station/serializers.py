from rest_framework import serializers
from . import models


class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estacion
        fields = ('id',
                  'nombre',
                  'direccion',
                  'telefono',
                  'longitud',
                  'latitud'
                  )


class TipoCombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoCombustible
        fields = ('id',
                  'nombre'
                  )


class EstacionCombustibleSerializer(serializers.ModelSerializer):
    estacion_nombre = serializers.CharField(
        source='estacion.nombre',
        read_only=True
    )
    tipo_combustible_nombre = serializers.CharField(
        source='tipo_combustible.nombre',
        read_only=True
    )

    class Meta:
        model = models.EstacionCombustible
        fields = ('id',
                  'estacion',
                  'estacion_nombre',
                  'tipo_combustible_nombre',
                  'tipo_combustible',
                  'valor'
                  )
