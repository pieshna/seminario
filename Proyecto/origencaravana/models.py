from django.db import models

# Create your models here.

class Origencaravana(models.Model):
    idcaravana = models.AutoField(db_column='IdCaravana', primary_key=True)  # Field name made lowercase.
    lugar = models.CharField(db_column='Lugar', max_length=60)  # Field name made lowercase.

    

    class Meta:
        managed = False
        db_table = 'origencaravana'