from .models import Poblacion
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import PoblacionForm
from django.shortcuts import redirect
 
class StaffRequiredMixin(object):
    #Esto es un Mixin que requerirá ser usuario miembro del staff o ADM para dar acceso a la funcionalidad
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_staff or request.user.persona.tipoPerfil=='ADM'):
                return redirect(reverse_lazy('admin:login'))
            return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('restricted'))

class poblacionListView(ListView):
    model = Poblacion
    paginate_by = 3

class poblacionCreate(StaffRequiredMixin,CreateView):
    model = Poblacion
    form_class = PoblacionForm
    success_url = reverse_lazy('poblaciones:poblaciones')
 

class poblacionUpdate(StaffRequiredMixin,UpdateView):
    model = Poblacion
    form_class = PoblacionForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('poblaciones:poblaciones')

    def get_success_url(self):
        return reverse_lazy('poblaciones:editar',args=[self.object.id]) +'?ok'

