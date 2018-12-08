from django.contrib import admin
from .models import Poblacion
# Register your models here.

class PoblacionAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')

    list_display = ('nombre','provincia','comunidadAutonoma','codigoPostal','avatar')
    ordering = ('comunidadAutonoma','provincia','nombre')
    search_fields = ('codigoPostal','provincia','comunidadAutonoma','nombre')

admin.site.register(Poblacion,PoblacionAdmin)