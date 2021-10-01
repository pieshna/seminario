from django.db import models

# Create your models here.

class Diasdevoluntariado(models.Model):
    iddia = models.AutoField(db_column='IdDia', primary_key=True)  # Field name made lowercase.
    diaarealizar = models.DateField(db_column='DiaARealizar')  # Field name made lowercase.
    fkidvoluntario = models.IntegerField(db_column='FkIdVoluntario')  # Field name made lowercase.
    fkidusuario = models.IntegerField(db_column='FkIdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diasdevoluntariado'