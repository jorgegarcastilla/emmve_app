from django.contrib import admin
from .models import Aula
# Register your models here.

class AulaAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')

    list_display = ('nombre','superficie','aforo','poblacion','imagen')
    ordering = ('nombre','superficie','superficie')
    search_fields = ('nombre','poblacion')

admin.site.register(Aula,AulaAdmin)
