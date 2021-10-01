from django.db import models

# Create your models here.

class Horasdevoluntariado(models.Model):
    idhoras = models.AutoField(db_column='IdHoras', primary_key=True)  # Field name made lowercase.
    fkidpersona = models.IntegerField(db_column='FKIdPersona')  # Field name made lowercase.
    fkidusuario = models.IntegerField(db_column='FKIdUsuario')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.
    horasrealizadas = models.IntegerField(db_column='HorasRealizadas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horasdevoluntariado'