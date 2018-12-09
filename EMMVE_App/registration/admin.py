from django.contrib import admin
from .models import Persona,Gestor,Docente

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('nombre','primerApellido','segundoApellido','dni','telefonoPrincipal','tipoPerfil')
    ordering = ('tipoPerfil','nombre','primerApellido','segundoApellido')
    search_fields = ('primerApellido','segundoApellido','tipoPerfil')


class GestorAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')

    list_display = ('nombre','primerApellido','segundoApellido','dni','telefonoPrincipal')
    ordering = ('nombre','primerApellido','segundoApellido')
    search_fields = ('primerApellido','segundoApellido')

class DocenteAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')

    list_display = ('nombre','primerApellido','segundoApellido','dni','telefonoPrincipal')
    ordering = ('nombre','primerApellido','segundoApellido')
    search_fields = ('primerApellido','segundoApellido')


admin.site.register(Persona,PersonaAdmin)
admin.site.register(Gestor,GestorAdmin)
admin.site.register(Docente,DocenteAdmin)

