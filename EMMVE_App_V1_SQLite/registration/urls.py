from django.urls import path,include
from .views import  SignUpView, ProfileUpdate, docenteListView,docenteCreate,docenteUpdate

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'), #profile  es el path al que django nos redirecciona al hacer login.
    path('docentes/',docenteListView.as_view(), name='docentes'),
    path('docentes/create/',docenteCreate.as_view(), name='docentesCrear'),
    path('docentes/update/<int:pk>/',docenteUpdate.as_view(), name='docentesEditar'),    
]