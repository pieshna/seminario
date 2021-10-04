from django.contrib import admin
from donacion.models import Donacion

# Register your models here.

class DonacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'direccion', 'descripcion', 'fechadeentrega', 'usuario']
    search_fields = ['nombre']

admin.site.register(Donacion, DonacionAdmin)