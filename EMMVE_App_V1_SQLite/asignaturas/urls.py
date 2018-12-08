from django.urls import path
from .views import AsignaturaListView, AsignaturaDetailView, AsignaturaCreate, AsignaturaUpdate

asignaturas_patterns = ([
    path('',AsignaturaListView.as_view(), name='asignaturas'),
    path('<int:pk>/<slug:slug>/', AsignaturaDetailView.as_view(), name='asignatura'),
    path('create/',AsignaturaCreate.as_view(), name='crear'),
    path('update/<int:pk>/',AsignaturaUpdate.as_view(), name='editar'),
],'asignaturas')