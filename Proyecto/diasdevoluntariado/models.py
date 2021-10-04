# -*- coding: utf-8 -*-
from django.db import models
from voluntario.models import Voluntario


# Create your models here.

class Diasdevoluntariado(models.Model):
    iddia = models.AutoField(db_column='IdDia', primary_key=True) 
    diaarealizar = models.CharField('Día a Realizar', db_column='DiaARealizar', max_length=15)
    horasaprox = models.CharField('Horas aprox', db_column='HorasAprox', max_length=10) 
    voluntario = models.ForeignKey(Voluntario, models.DO_NOTHING, db_column='FkIdVoluntario')


    def __str__(self):
        return '%s' % (self.voluntario)

    class Meta:
        verbose_name = 'Día de Voluntariado'
        verbose_name_plural = 'Días de Voluntariado'
        managed = False
        db_table = 'diasdevoluntariado'