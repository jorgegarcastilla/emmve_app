from django import forms
from .models import Asignatura

class AsignaturaForm(forms.ModelForm):

    class Meta:
        model = Asignatura
        fields = '__all__'
        widgets = {
        'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar el nombre de la asignatura'}),
        'image':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        'nivel':forms.Select(attrs={'class':'form-control mt-3'}),
        'curso':forms.Select(attrs={'class':'form-control mt-3'}),
        'sesionesSemanales':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar el número de sesiones o clases semanales'}),
        'duracion':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar la duración en minutos de cada sesión o clase'}),
        'aforoMaximo':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar el número máximo de alumnos por grupo'}),
        'aforoMinimo':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar el número mínimo de alumnos por grupo'}),
        'edadMinima':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar la edad mínima teorica para cursar la asignatura'}),
        'edadMaxima':forms.NumberInput(attrs={'class':'form-control mt-3','placeholder':'Indicar la edad máxima teorica para cursar la asignatura'}),            
        }
        labels = {
        'nombre':'',
        'image':'',
        'nivel':'',
        'curso':'',
        'sesionesSemanales':'',
        'duracion':'',
        'aforoMaximo':'',
        'aforoMinimo':'',
        'edadMinima':'',
        'edadMaxima':'',
        } 
