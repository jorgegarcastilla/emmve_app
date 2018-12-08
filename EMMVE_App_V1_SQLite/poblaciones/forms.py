from django import forms
from .models import Poblacion

class PoblacionForm(forms.ModelForm):

    class Meta:
        model = Poblacion
        fields = ['nombre','codigoPostal','provincia','comunidadAutonoma','avatar']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre de la población'}),
            'codigoPostal':forms.TextInput (attrs={'class':'form-control mt-3', 'placeholder':'Código Postal'}),
            'provincia':forms.TextInput (attrs={'class':'form-control mt-3', 'placeholder':'Provincia'}),
            'comunidadAutonoma':forms.TextInput (attrs={'class':'form-control mt-3', 'placeholder':'Comunidad autónoma'}),         
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
         }
