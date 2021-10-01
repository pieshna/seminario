from django.db import models
from diasdevoluntariado.models import Diasdevoluntariado
from horasdevoluntariado.models import Horasdevoluntariado
from creencias.models import Creencias

# Create your models here.

class Voluntario(models.Model):
    idvoluntario = models.AutoField(db_column='IdVoluntario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=16)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=50)  # Field name made lowercase.
    fkidusuario = models.IntegerField(db_column='FKIdUsuario')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=75)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=120)  # Field name made lowercase.
    fkdiavoluntariado = models.ForeignKey(Diasdevoluntariado, models.DO_NOTHING, db_column='FKDiaVoluntariado')  # Field name made lowercase.
    tipovoluntario = models.CharField(db_column='TipoVoluntario', max_length=20)  # Field name made lowercase.
    fkhoras = models.ForeignKey(Horasdevoluntariado, models.DO_NOTHING, db_column='FKHoras')  # Field name made lowercase.
    fkcreenciasreligiosas = models.ForeignKey(Creencias, models.DO_NOTHING, db_column='FKCreenciasReligiosas')  # Field name made lowercase.
    
    def __str__(self):
        return '%s %s %s %s %s' % (self.nombre, self.apellido, self.fkdiavoluntariado, self.fkhoras, self.fkcreenciasreligiosas)

    class Meta:
        managed = False
        db_table = 'voluntario'