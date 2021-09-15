from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Bitacora(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    fk_id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='fk_id_usuario')
    descripcion = models.IntegerField()
    created_at = models.IntegerField()
    updated_at = models.IntegerField()

    class Meta:
        verbose_name = 'bitacora'
        verbose_name_plural = 'bitacoras'
        managed = False
        db_table = 'bitacora'