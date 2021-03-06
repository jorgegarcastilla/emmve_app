from django.urls import path
from .views import NoticiaListView, NoticiaDetailView, NoticiaCreate, NoticiaUpdate, NoticiaDelete

noticias_patterns = ([
    path('',NoticiaListView.as_view(), name='noticias'),
    path('<int:pk>/<slug:slug>/', NoticiaDetailView.as_view(), name='noticia'),
    path('create/',NoticiaCreate.as_view(), name='crear'),
    path('update/<int:pk>/',NoticiaUpdate.as_view(), name='editar'),
    path('delete/<int:pk>/',NoticiaDelete.as_view(), name='eliminar'),
],'noticias')