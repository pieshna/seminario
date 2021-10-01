from django.contrib import admin
from migrante.models import Migrante
# Register your models here.

class MigranteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido', 'telefono', 'genero', 'edad', 'nacionalidad']
    list_filter = ['genero',]
    search_fields = ['nombre','apellido']

admin.site.register(Migrante, MigranteAdmin)