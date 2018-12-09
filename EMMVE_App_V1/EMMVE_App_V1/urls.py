"""EMMVE_App_V1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from core import views as core_views #J.G.CASTILLA: Se importan las vistas de core.
from noticias.urls import noticias_patterns
from poblaciones.urls import poblaciones_patterns
from aulas.urls import aulas_patterns
from asignaturas.urls import asignaturas_patterns
from alumnos.urls import alumnos_patterns
from disponibilidades.urls import disponibilidades_patterns
from docentes.urls import docentes_patterns

from django.conf import settings #J.G.CASTILLA : Se importa el archivo de settings del proyecto para poder consultar algunos valores de configuración.

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('team/', core_views.team, name="team"),
    path('restricted/', core_views.accesoRestringido, name="restricted"),
    path('admin/', admin.site.urls),
    path('noticias/', include(noticias_patterns)),
    path('asignaturas/', include(asignaturas_patterns)),
    path('poblaciones/', include(poblaciones_patterns)),
    path('docentes/', include(docentes_patterns)),
    path('disponibilidades/', include(disponibilidades_patterns)),
    path('aulas/', include(aulas_patterns)),
    path('alumnos/', include(alumnos_patterns)),
    path('accounts/',include('registration.urls')),
]


#J.G.CASTILLA : PARA QUE EL SERVIDOR WEB DE DJANGO PUEDA SERVIR IMÁGENES EN MODO DEBUG LE INDICAMOS LAS RUTAS DONDE DEBE BUSCAR LOS FICHEROS MEDIA.
if settings.DEBUG:
    from django.conf.urls.static import static #Nos permite acceder a las imágenes desde el administrador
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "EMMVE WEB App"
admin.site.index_title = "Panel de Administración"
admin.site.site_title = "EMMVE WEB App"