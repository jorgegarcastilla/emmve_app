from django.urls import path
from .views import docenteListView, docenteCreate, docenteUpdate

docentes_patterns = ([
    path('docentes/',docenteListView.as_view(), name='docentes'),
    path('create/',docenteCreate.as_view(), name='crear'),
    path('update/<int:pk>/',docenteUpdate.as_view(), name='editar'),
],'docentes')