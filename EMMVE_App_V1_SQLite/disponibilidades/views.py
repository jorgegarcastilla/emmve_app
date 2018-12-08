
from .models import DisponibilidadAlumno,DisponibilidadDocente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DisponibilidadDocenteForm
from django.shortcuts import redirect
 
# Create your views here.
class StaffRequiredMixin(object):
    #Esto es un Mixin que requerirá ser usuario miembro del staff o ADM para dar acceso a la funcionalidad
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_staff or request.user.persona.tipoPerfil=='DOC' or request.user.persona.tipoPerfil=='GES'):
                return redirect(reverse_lazy('admin:login'))
            return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('restricted'))
        

class DisponibilidadDocenteListView(ListView):
    model = DisponibilidadDocente
    paginate_by = 10

    def get_queryset(self):

        return DisponibilidadDocente.objects.filter(docente_id=self.request.user.persona.id)

# class DisponibilidadAlumnoListView(ListView):
#     model = DisponibilidadAlumno
#     paginate_by = 10

#     def get_queryset(self):
#     return DisponibilidadAlumno.objects.filter(alumno=self.request.user.persona.id)

class DisponibilidadDocenteCreate(StaffRequiredMixin,CreateView):
    model = DisponibilidadDocente
    form_class = DisponibilidadDocenteForm
    success_url = reverse_lazy('disponibilidades:disponibilidadesDocente')

    def post(self, request, *args, **kwargs):
        # disponibilidadDocente = DisponibilidadDocente()
        # print(disponibilidadDocente)
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            disponibilidadDocente = form.save(commit=False)
            disponibilidadDocente.docente_id = request.user.persona.id
            disponibilidadDocente.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))   

# class DisponibilidadAlumnoCreate(StaffRequiredMixin,CreateView):
#     model = DisponibilidadAlumno
#     form_class = DisponibilidadForm
#     success_url = reverse_lazy('disponibilidades:disponibilidades')

class DisponibilidadDocenteUpdate(StaffRequiredMixin,UpdateView):
    model = DisponibilidadDocente
    form_class = DisponibilidadDocenteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('disponibilidades:disponibilidadesDocente')

    def get_success_url(self):
        return reverse_lazy('disponibilidades:editarDocente',args=[self.object.id]) +'?ok'

# class DisponibilidadAlumnoUpdate(StaffRequiredMixin,UpdateView):
#     model = DisponibilidadAlumno
#     form_class = DisponibilidadForm
#     template_name_suffix = '_update_form'
#     success_url = reverse_lazy('disponibilidades:disponibilidades')

#     def get_success_url(self):
#         return reverse_lazy('disponibilidades:editarAlumno',args=[self.object.id]) +'?ok'

class DisponibilidadDocenteDelete(StaffRequiredMixin,DeleteView):
    model = DisponibilidadDocente
    success_url = reverse_lazy('disponibilidades:disponibilidadesDocente')

# class DisponibilidadAlumnoDelete(StaffRequiredMixin,DeleteView):
#     model = DisponibilidadAlumno
#     success_url = reverse_lazy('disponibilidades:disponibilidades')