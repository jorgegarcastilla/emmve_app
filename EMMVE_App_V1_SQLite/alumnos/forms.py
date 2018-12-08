from django import forms
from .models import Alumno, Alumno_Gestor

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre','primerApellido','segundoApellido','fechaNacimiento','centroEstudios','empadronado','autorizaImagen', \
        'fichaMedica', 'content' ]
        widgets = {
        'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar el nombre del alumno'}),
        'primerApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar el nombre del alumno'}),
        'segundoApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar el nombre del alumno'}),
        'fechaNacimiento':forms.DateInput(attrs={'class':'form-control mt-3', 'placeholder':'Seleccionar fecha de nacimiento del alumno'}),
        'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        'gestor':forms.Select(attrs={'class':'form-control mt-3'}),            
        'tutor':forms.Select(attrs={'class':'form-control mt-3'}),
        'genero':forms.Select(attrs={'class':'form-control mt-3'}),
        'centroEstudios':forms.Select(attrs={'class':'form-control mt-3'}),
        'empadronado':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        'autorizaImagen':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        'fichaMedica':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        'content':forms.Textarea(attrs={'class':'form-control mt-3','placeholder':'Indicar conocimientos musicales previos del alumno'}),
        }
        labels = {
        'nombre':'',
        'primerApellido':'',
        'segundoApellido':'',
        'fechaNacimiento':'',
        'content':'',
        }

class AlumnoGestorForm(forms.ModelForm):
    class Meta:
        model = Alumno_Gestor
        fields = ['rol','esGestor','esPagador','recibeNotificaciones','domicilioHabitual']
        widgets = {
        'rol':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indique su rol con el alumno'}),
        'esGestor':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        'esPagador':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        'recibeNotificaciones':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),            
        'domicilioHabitual':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
        }
 