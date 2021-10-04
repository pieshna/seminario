from django.contrib import admin
from asistencia.models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['voluntario', 'entrada', 'salida']
    search_fields = ['voluntario']

admin.site.register(Asistencia, AsistenciaAdmin)
