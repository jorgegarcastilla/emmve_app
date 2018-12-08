from django.contrib import admin
from .models import Noticia

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    # Indicamos campos que queremos que aparezcan en el administrador como no editables.
    readonly_fields = ('created','updated')
    list_display = ('updated', 'titulo')
    ordering = ('-updated',)
    search_fields = ('titulo','content')

    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('noticias/css/custom_ckeditor.css',)
        }
        

admin.site.register(Noticia,NoticiaAdmin)