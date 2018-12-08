from django.urls import path
from .views import aulaListView, aulaCreate, aulaUpdate

aulas_patterns = ([
    path('',aulaListView.as_view(), name='aulas'),
    path('create/',aulaCreate.as_view(), name='crear'),
    path('update/<int:pk>/',aulaUpdate.as_view(), name='editar'),
],'aulas')