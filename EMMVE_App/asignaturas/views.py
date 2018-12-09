from .models import Asignatura
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AsignaturaForm
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

class AsignaturaListView(ListView):
    model = Asignatura
    paginate_by = 3

class AsignaturaDetailView(DetailView):
    model = Asignatura

class AsignaturaCreate(StaffRequiredMixin,CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    success_url = reverse_lazy('asignaturas:asignaturas')
 

class AsignaturaUpdate(StaffRequiredMixin,UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('asignaturas:asignaturas')

    def get_success_url(self):
        return reverse_lazy('asignaturas:editar',args=[self.object.id]) +'?ok'

class AsignaturaDelete(StaffRequiredMixin,DeleteView):
    model = Asignatura
    success_url = reverse_lazy('asignaturas:asignaturas')