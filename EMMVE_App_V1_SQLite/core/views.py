from django.shortcuts import render, HttpResponse
from registration.models import Docente

# Create your views here.

def home(request):
    print(request.user)    
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def team(request):    
    docentes = Docente.objects.filter(tipoPerfil='DOC',activo=True) 
    return render(request, "core/team.html",{'docentes':docentes})    

def accesoRestringido(request):
    return render(request, "core/notAuthorized.html")


