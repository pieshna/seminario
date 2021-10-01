from django.db import models

# Create your models here.

class Donacion(models.Model):
    iddonacion = models.AutoField(db_column='IdDonacion', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=18)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=254)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=254)  # Field name made lowercase.
    fechadeentrega = models.DateTimeField(db_column='FechaDeEntrega')  # Field name made lowercase.
    fkidusuario = models.IntegerField(db_column='FKIdUsuario')  # Field name made lowercase.

    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        managed = False
        db_table = 'donacion'