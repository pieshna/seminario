from django.contrib import admin
from voluntario.models import Voluntario

# Register your models here.

class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'telefono', 'genero', 'edad', 'fechanacimiento', 'nacionalidad', 'correo', 'direccion', 'tipovoluntario', 'creencias', 'usuario']
    list_filter = ['genero']
    search_fields = ['nombre', 'apellido']

admin.site.register(Voluntario, VoluntarioAdmin)