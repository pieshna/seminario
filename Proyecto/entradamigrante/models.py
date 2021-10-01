from django.db import models
from migrante.models import Migrante
from modulo.models import Modulo

# Create your models here.

class Entradamigrante(models.Model):
    idmovilidad = models.AutoField(db_column='IdMovilidad', primary_key=True)  # Field name made lowercase.
    fkidmigrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FkIdMigrante')  # Field name made lowercase.
    fechaentrada = models.DateTimeField(db_column='FechaEntrada')  # Field name made lowercase.
    fkidmodulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='FkIdModulo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=254)  # Field name made lowercase.

    def __str__(self):
        return '%s %s' % (self.fkidmigrante, self.fkidmodulo)

    class Meta:
        managed = False
        db_table = 'entradamigrante'