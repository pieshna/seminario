from django.db import models

# Create your models here.

class Migrante(models.Model):
    idmigrante = models.AutoField(db_column='IdMigrante', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=16)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=50)  # Field name made lowercase.
    fkidusuario = models.IntegerField(db_column='FKIdUsuario')  # Field name made lowercase.

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    class Meta:
        managed = False
        db_table = 'migrante'