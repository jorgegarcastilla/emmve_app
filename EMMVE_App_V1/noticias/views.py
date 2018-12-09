
from .models import Noticia
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import NoticiaForm
from django.shortcuts import redirect
 
# Create your views here.
class StaffRequiredMixin(object):
    #Esto es un Mixin que requerirá ser usuario miembro del staff o ADM para dar acceso a la funcionalidad
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_staff or request.user.persona.tipoPerfil=='ADM'):
                return redirect(reverse_lazy('admin:login'))
            return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('restricted'))
        

class NoticiaListView(ListView):
    model = Noticia
    paginate_by = 3

class NoticiaDetailView(DetailView):
    model = Noticia

class NoticiaCreate(StaffRequiredMixin,CreateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticias')

 

class NoticiaUpdate(StaffRequiredMixin,UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('noticias:noticias')

    def get_success_url(self):
        return reverse_lazy('noticias:editar',args=[self.object.id]) +'?ok'

class NoticiaDelete(StaffRequiredMixin,DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:noticias')