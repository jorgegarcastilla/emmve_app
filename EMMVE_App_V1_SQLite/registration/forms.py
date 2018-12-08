from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gestor,Docente,Persona
from poblaciones.models import Poblacion

class UserCreationFormWithEmail (UserCreationForm):
    email = forms.EmailField(required=True,help_text="Requerido, máximo 254 caracteres y válido")

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    # debemos poner clean y el campo en el nombre de la def
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists(): # Hacemos una consulta para ver si exite algún usuario con ese e-mail
            raise forms.ValidationError("El email está registrado, por favor prueba con otro")
        return email

class UserCreationGestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['nombre','primerApellido','segundoApellido','dni','telefonoPrincipal','direccion','poblacion']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar nombre'}),
            'primerApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar primer apellido'}),
            'segundoApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar segundo apellido'}),
            'dni':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introducir el D.N.I'}),
            'telefonoPrincipal':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca su telefono de contacto'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar dirección postal'}),
            'poblacion':forms.Select(attrs={'class':'form-control mt-3'}),
        }
class GestorForm(forms.ModelForm):
    class Meta:
        model = Gestor
        fields = ['avatar','nombre','primerApellido','segundoApellido','dni','telefonoPrincipal','telefonoSecundario','direccion','poblacion', \
        'numeroCC','iban','swift','rentaBasica','familiaNumerosa']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar nombre'}),
            'primerApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar primer apellido'}),
            'segundoApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar segundo apellido'}),
            'dni':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introducir el D.N.I'}),
            'telefonoPrincipal':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca su telefono principal de contacto'}),
            'telefonoSecundario':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca un telefono secundario de contacto'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar dirección postal'}),
            'poblacion':forms.Select(attrs={'class':'form-control mt-3'}),
            'numeroCC':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indique su número de cuenta'}),
            'iban':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indique IBAN de la cuenta'}),
            'swift':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indique SWIFT de la cuenta'}),
            'rentaBasica':forms.CheckboxInput(attrs={'class':'form-control mt-3', 'placeholder':'Indique si cumple requisitos de renta básica'}),
            'familiaNumerosa':forms.CheckboxInput(attrs={'class':'form-control mt-3','placeholder':'Indique si cumple requisitos de familia numerosa'}),
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['avatar','nombre','primerApellido','segundoApellido','dni','telefonoPrincipal','telefonoSecundario','direccion','poblacion', \
        'link']
        widgets = {
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
        

class AdministrativoForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['avatar','nombre','primerApellido','segundoApellido','dni','telefonoPrincipal','telefonoSecundario','direccion','poblacion']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'nombre':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar nombre'}),
            'primerApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar primer apellido'}),
            'segundoApellido':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar segundo apellido'}),
            'dni':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introducir el D.N.I'}),
            'telefonoPrincipal':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca su telefono principal de contacto'}),
            'telefonoSecundario':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Introduzca un telefono secundario de contacto'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar dirección postal'}),
            'poblacion':forms.Select(attrs={'class':'form-control mt-3'}),
        }

class ADM_DocenteForm(forms.ModelForm):

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