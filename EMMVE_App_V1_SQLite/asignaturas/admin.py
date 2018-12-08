from django.contrib import admin
from .models import Asignatura

# Register your models here.
class AsignaturaAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('nombre', 'nivel', 'curso','sesionesSemanales','duracion')
    ordering = ('nombre', 'nivel', 'curso','sesionesSemanales','duracion')
    search_fields = ('nombre', 'nivel', 'curso')

admin.site.register(Asignatura,AsignaturaAdmin)

