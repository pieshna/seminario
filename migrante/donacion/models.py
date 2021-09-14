from django.db import models
from usuarios.models import Usuarios

# Create your models here.
class Donacion(models.Model):
    id_donacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=254)
    lugar = models.CharField(max_length=120)
    tipo_donacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fk_id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='fk_id_usuario')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'donacion'
        verbose_name_plural = 'donaciones'
        managed = False
        db_table = 'donacion'