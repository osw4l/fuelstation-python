from django.db import models

# Create your models here.


class Estacion(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    longitud = models.CharField(max_length=20)
    latitud = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Estacion de servicio'
        verbose_name_plural = 'Estaciones de servicio'

    def __str__(self):
        return '{} {}'.format(self.nombre, self.direccion)


class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Tipo de combustible'
        verbose_name_plural = 'Tipos de combustible'

    def __str__(self):
        return self.nombre


class EstacionCombustible(models.Model):
    estacion = models.ForeignKey(Estacion)
    tipo_combustible = models.ForeignKey(TipoCombustible)
    valor = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Combustible de estacion'
        verbose_name_plural = 'Combustibles de estaciones'
        unique_together = ['estacion', 'tipo_combustible', 'valor']

