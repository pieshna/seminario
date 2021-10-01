from django.db import models
from migrante.models import Migrante
from pais.models import Pais
from origencaravana.models import Origencaravana

# Create your models here.

class Caravanamigrante(models.Model):
    idcaravana = models.AutoField(db_column='IdCaravana', primary_key=True)  # Field name made lowercase.
    fkidmigrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FkIdMigrante')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    fkidpais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='FkIdPais')  # Field name made lowercase.
    fkorigen = models.ForeignKey(Origencaravana, models.DO_NOTHING, db_column='FkOrigen')  # Field name made lowercase.

    def __str__(self):
        return '%s %s %s %s' % (self.fkidmigrante, self.fkidpais, self.fkorigen, self.nombre)
        
    class Meta:
        managed = False
        db_table = 'caravanamigrante'