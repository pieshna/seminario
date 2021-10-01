from django.db import models

# Create your models here.

class Pais(models.Model):
    idpais = models.AutoField(db_column='IdPais', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        managed = False
        db_table = 'pais'