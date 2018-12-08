from django.urls import path
from .views import DisponibilidadDocenteListView, DisponibilidadDocenteCreate, DisponibilidadDocenteUpdate, DisponibilidadDocenteDelete
disponibilidades_patterns = ([
    path('docente/',DisponibilidadDocenteListView.as_view(), name='disponibilidadesDocente'),
    path('docente/create/',DisponibilidadDocenteCreate.as_view(), name='crearDocente'),
    path('docente/update/<int:pk>/',DisponibilidadDocenteUpdate.as_view(), name='editarDocente'),
    path('docente/delete/<int:pk>/',DisponibilidadDocenteDelete.as_view(), name='eliminarDocente'),
],'disponibilidades')