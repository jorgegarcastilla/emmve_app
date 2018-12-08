from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    list_display = ('clave','nombre','url')
    ordering = ('clave',)
    search_fields = ('clave',)
    
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_staff:
            return ('clave', 'nombre')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)