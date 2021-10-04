from django.db import models
from voluntario.models import Voluntario

# Create your models here.

class Asistencia(models.Model):
    idasistencia = models.AutoField(db_column='IdAsistencia', primary_key=True)  # Field name made lowercase.
    voluntario = models.ForeignKey(Voluntario, models.DO_NOTHING, db_column='FKIdVoluntario')  # Field name made lowercase.
    entrada = models.TimeField('Entrada', db_column='Entrada')  # Field name made lowercase.
    salida = models.TimeField('Salida', db_column='Salida')  # Field name made lowercase.


    def __str__(self):
        return '%s' % (self.voluntario)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        managed = False
        db_table = 'asistencia'