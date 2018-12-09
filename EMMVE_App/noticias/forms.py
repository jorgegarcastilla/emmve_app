from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo','content','image']
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Indicar el título de la noticia'}),
            'content':forms.Textarea(attrs={'class':'form-control mt-3'}),            
            'image':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
         }
        labels = {
            'titulo':'',
            'content':'',            
            'image':'',
         }