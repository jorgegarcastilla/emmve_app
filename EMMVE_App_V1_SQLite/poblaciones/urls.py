from django.urls import path
from .views import poblacionListView, poblacionCreate, poblacionUpdate

poblaciones_patterns = ([
    path('',poblacionListView.as_view(), name='poblaciones'),
    path('create/',poblacionCreate.as_view(), name='crear'),
    path('update/<int:pk>/',poblacionUpdate.as_view(), name='editar'),
],'poblaciones')