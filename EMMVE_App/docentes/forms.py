from django import forms
from registration.models import Docente

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente
        fields = ['user','tipoPerfil','activo','rolDirector','rolJefatura','jornada','avatar','nombre','primerApellido', \
        'segundoApellido','dni','telefonoPrincipal','telefonoSecundario','direccion','poblacion','link']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control mt-3'}),
            'tipoPerfil':forms.Select(attrs={'class':'form-control mt-3'}),
            'activo':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
            'rolDirector':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
            'rolJefatura':forms.CheckboxInput(attrs={'class':'form-control mt-3'}),
            'jornada':forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar jornada en "%" '}),
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar nombre'}),
            'primerApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar primer apellido'}),
            'segundoApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar segundo apellido'}),
            'dni':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introducir el D.N.I'}),
            'telefonoPrincipal':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca su telefono principal de contacto'}),
            'telefonoSecundario':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca un telefono secundario de contacto'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar dirección postal'}),
            'poblacion':forms.Select(attrs={'class':'form-control mt-3'}),
            'link':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar link a la página de información profesional'}),
        } 

 