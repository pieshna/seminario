from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Caravanamigrante(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    fk_id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='fk_id_usuario')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'caravanamigrante'
        verbose_name_plural = 'caravanasmigrantes'
        managed = False
        db_table = 'caravanamigrante'