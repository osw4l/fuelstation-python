# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-12 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='estacioncombustible',
            unique_together=set([('estacion', 'tipo_combustible')]),
        ),
    ]