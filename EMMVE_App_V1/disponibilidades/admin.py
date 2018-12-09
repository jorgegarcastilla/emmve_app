from django.contrib import admin
from .models import Disponibilidad,DisponibilidadDocente,DisponibilidadAlumno

# Register your models here.
class DisponibilidadAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')

    ordering = ('-cursoAcademico','diaSemana','horaInicio')
    search_fields = ('cursoAcademico','diaSemana')

class DisponibilidadDocenteAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('docente','diaSemana','horaInicio', 'horaFin','cursoAcademico')
    ordering = ('-cursoAcademico','diaSemana','horaInicio')
    search_fields = ('cursoAcademico','diaSemana')

class DisponibilidadAlumnoAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('alumno','diaSemana','horaInicio', 'horaFin','cursoAcademico')
    ordering = ('-cursoAcademico','diaSemana','horaInicio')
    search_fields = ('cursoAcademico','diaSemana')   

admin.site.register(Disponibilidad,DisponibilidadAdmin)
admin.site.register(DisponibilidadDocente,DisponibilidadDocenteAdmin)
admin.site.register(DisponibilidadAlumno,DisponibilidadAlumnoAdmin)
