from django.contrib import admin
from caravanamigrante.models import Caravanamigrante


# Register your models here.



class CaravanamigranteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'país', 'origen']
    list_filter = ['país']
    search_fields = ['nombre', 'país']
    

admin.site.register(Caravanamigrante, CaravanamigranteAdmin)