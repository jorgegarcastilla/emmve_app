from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):

    class Meta:
        model = Aula
        fields = ['nombre','superficie','aforo','poblacion','imagen']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre del aula'}),
            'superficie':forms.NumberInput (attrs={'class':'form-control mt-3', 'placeholder':'Superficie en m2'}),
            'aforo':forms.NumberInput (attrs={'class':'form-control mt-3', 'placeholder':'Aforo máximo'}),
            'poblacion':forms.Select (attrs={'class':'form-control mt-3'}),         
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
         }
