from django.db import models
# Create your models here.

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=75)
    password = models.CharField(max_length=254)
    username = models.CharField(max_length=20)
    foto = models.CharField(max_length=254)
    fecha_nacimiento = models.DateField()
    estado = models.IntegerField()
    rol = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.nombre}{self.apellido}'

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'usuarios'
        managed = False 
        #Hola 
        
