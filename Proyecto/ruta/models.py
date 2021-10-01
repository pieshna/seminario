from django.db import models

# Create your models here.

class Ruta(models.Model):
    idruta = models.AutoField(db_column='IdRuta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return '%s %s' % (self.nombre, self.destino)

    class Meta:
        managed = False
        db_table = 'ruta'