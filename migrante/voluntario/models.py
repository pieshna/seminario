from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Voluntario(models.Model):
    id_voluntariolocal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    creencias_religiosas = models.CharField(max_length=50)
    horas_acumuladas = models.IntegerField()
    dia_de_voluntariado = models.IntegerField()
    pais_origen = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)
    fk_id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='fk_id_usuario')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'voluntario'
        verbose_name_plural = 'voluntarios'
        managed = False
        db_table = 'voluntario'