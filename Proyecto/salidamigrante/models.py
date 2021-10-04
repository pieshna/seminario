# -*- coding: utf-8 -*-
from django.db import models
from migrante.models import Migrante
from ruta.models import Ruta

# Create your models here.

class Salidamigrante(models.Model):
    idsalida = models.AutoField(db_column='IdSalida', primary_key=True) 
    migrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FKIdMigrante')  
    fechasalida = models.DateTimeField('Fecha de Salida', db_column='FechaSalida')  
    ruta = models.ForeignKey(Ruta, models.DO_NOTHING, db_column='FkIdRuta') 

    def __str__(self):
        return '%s %s' % (self.migrante, self.ruta)


    class Meta:
        verbose_name = 'Salida de Migrante'
        verbose_name_plural = 'Salidas de Migrante'
        managed = False
        db_table = 'salidamigrante'