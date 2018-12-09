from django.contrib import admin
from .models import Alumno,Alumno_Gestor

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('nombre', 'primerApellido', 'segundoApellido','tutor','empadronado')#BUSCAR COMO INCLUIR EL NOMBRE DE SU GESTOR MANY_TO_MANY
    ordering = ('primerApellido','segundoApellido','nombre','fechaNacimiento')
    search_fields = ('primerApellido','segundoApellido','Nombre','tutor','gestor')
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('alumnos/css/custom_ckeditor.css',)
        }

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Alumno_Gestor)