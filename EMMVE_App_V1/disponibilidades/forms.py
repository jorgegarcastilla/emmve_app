from django import forms
from .models import DisponibilidadDocente

class DisponibilidadDocenteForm(forms.ModelForm):

    class Meta:
        model = DisponibilidadDocente
        fields = ['diaSemana','horaInicio','horaFin','cursoAcademico','docente']
        widgets = {
            'horaInicio':forms.TimeInput(attrs={'class':'form-control mt-3','placeholder':'HH:MM'}),
            'horaFin':forms.TimeInput(attrs={'class':'form-control mt-3','placeholder':'HH:MM'}),            
            'diaSemana':forms.Select(attrs={'class':'form-control-file mt-3'}),
            'cursoAcademico':forms.NumberInput(attrs={'class':'form-control-file mt-3','placeholder':'AAAA'}),
            'docente':forms.HiddenInput(),
         }
        labels = {
            'horaInicio':'Desde',
            'horaFin':'Hasta',            
            'diaSemana':'Dia',
            'cursoAcademico':'Año inicio del curso',
         }
