from registration.models import Docente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import DocenteForm
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

class docenteListView(ListView):
    model = Docente
    paginate_by = 3
    def get_queryset(self):
        return Docente.objects.filter(tipoPerfil='DOC',activo=True)

class docenteCreate(StaffRequiredMixin,CreateView):
    model = Docente
    form_class = DocenteForm
    success_url = reverse_lazy('docentes:docentes')
 

class docenteUpdate(StaffRequiredMixin,UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('docentes:docentes')

    def get_success_url(self):
        return reverse_lazy('docentes:editar',args=[self.object.id]) +'?ok'

