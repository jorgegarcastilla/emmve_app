from django.urls import path
from .views import AlumnoListView, AlumnoDetailView, AlumnoCreate, AlumnoUpdate, AlumnoGestorCreate
from .views import AlumnoGestorListView,AlumnoTutorListView
alumnos_patterns = ([
    # path('misAlumnosGestionados/<int:pk>/',AlumnoPersonaListView.as_view(), name='misAlumnos'),
    path('misAlumnosGestionados/',AlumnoGestorListView.as_view(), name='misAlumnos'),
    path('misAlumnosTutelados/',AlumnoTutorListView.as_view(), name='misAlumnosTutelados'),
    path('gestionarNuevoAlumno/',AlumnoGestorCreate.as_view(), name='gestionarNuevoAlumno'),
    path('update/<int:pk>/',AlumnoUpdate.as_view(), name='editarMiAlumno'),
    path('<int:pk>/<slug:slug>/', AlumnoDetailView.as_view(), name='alumno'),
    path('', AlumnoListView.as_view(), name='alumnos'),
    path('create/',AlumnoCreate.as_view(), name='crear'),
    path('update/<int:pk>/',AlumnoUpdate.as_view(), name='editar'),
],'alumnos')