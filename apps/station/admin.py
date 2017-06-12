from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Estacion)
class EstacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'direccion', 'telefono']


@admin.register(models.TipoCombustible)
class TipoCombustible(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(models.EstacionCombustible)
class EstacionCombustible(admin.ModelAdmin):
    list_display = ['id', 'estacion', 'tipo_combustible', 'valor']

