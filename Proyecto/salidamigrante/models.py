from django.db import models
from migrante.models import Migrante
from ruta.models import Ruta

# Create your models here.

class Salidamigrante(models.Model):
    idsalida = models.AutoField(db_column='IdSalida', primary_key=True)  # Field name made lowercase.
    fkidmigrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FKIdMigrante')  # Field name made lowercase.
    fechasalida = models.DateTimeField(db_column='FechaSalida')  # Field name made lowercase.
    fkidruta = models.ForeignKey(Ruta, models.DO_NOTHING, db_column='FkIdRuta')  # Field name made lowercase.
    

    def __str__(self):
        return '%s %s' % (self.fkidmigrante, self.fkidruta)


    class Meta:
        managed = False
        db_table = 'salidamigrante'