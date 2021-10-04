# -*- coding: utf-8 -*-
from django.db import models
from creencias.models import Creencias
from authuser.models import AuthUser

# Create your models here.

class Voluntario(models.Model):
    idvoluntario = models.AutoField(db_column='IdVoluntario', primary_key=True) 
    nombre = models.CharField('Nombre', db_column='Nombre', max_length=50) 
    apellido = models.CharField('Apellido', db_column='Apellido', max_length=50)
    telefono = models.CharField('Teléfono', db_column='Telefono', max_length=16) 
    genero = models.CharField('Género', db_column='Genero', max_length=1) 
    edad = models.IntegerField('Edad', db_column='Edad') 
    fechanacimiento = models.DateField('Fecha de Nacimiento', db_column='FechaNacimiento') 
    nacionalidad = models.CharField('Nacionalidad', db_column='Nacionalidad', max_length=50)
    correo = models.CharField('Correo Electrónico', db_column='Correo', max_length=75)  
    direccion = models.CharField('Dirección', db_column='Direccion', max_length=120) 
    tipovoluntario = models.CharField('Tipo de Voluntario', db_column='TipoVoluntario', max_length=20)  
    creencias = models.ForeignKey(Creencias, models.DO_NOTHING, db_column='FKCreenciasReligiosas')  # Field name made lowercase.
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='FKIdUsuario')
    

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    class Meta:
        verbose_name = 'Voluntario'
        verbose_name_plural = 'Voluntarios'
        managed = False
        db_table = 'voluntario'