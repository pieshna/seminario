from django.db import models
from caravanamigrante.models import Caravanamigrante

# Create your models here.

class Movilidad(models.Model):
    id_movilidad = models.AutoField(primary_key=True)
    fk_id_persona = models.ForeignKey(Caravanamigrante, models.DO_NOTHING, db_column='fk_id_persona')
    nombre = models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    plan_movilidad = models.CharField(max_length=500)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    habitacion = models.CharField(max_length=3)
    locker = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'movilidad'
        verbose_name_plural = 'movilidades'
        managed = False
        db_table = 'movilidad'