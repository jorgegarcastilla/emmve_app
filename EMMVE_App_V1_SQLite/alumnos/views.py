
from .models import Alumno, Alumno_Gestor
from registration.models import Gestor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import AlumnoForm,AlumnoGestorForm
from django.shortcuts import redirect
 
# Create your views here.
class StaffRequiredMixin(object):
    #Esto es un Mixin que requerirá ser usuario miembro del staff o ADM para dar acceso a la funcionalidad
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_staff or request.user.persona.tipoPerfil=='ADM' or request.user.persona.tipoPerfil=='GES'):
                return redirect(reverse_lazy('admin:login'))
            return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('restricted'))

class AuthenticatedRequiredMixin(object):
    #Esto es un Mixin que requerirá ser usuario miembro del staff para dar acceso a la funcionalidad
   def dispatch(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('admin:login'))
        return super(AuthenticatedRequiredMixin,self).dispatch(request,*args,**kwargs)

class AlumnoListView(ListView):
    model = Alumno
    paginate_by = 3

class AlumnoDetailView(DetailView):
    model = Alumno

class AlumnoCreate(StaffRequiredMixin,CreateView):
    model = Alumno
    form_class = AlumnoForm
    success_url = reverse_lazy('alumnos:alumnos')
 

class AlumnoUpdate(StaffRequiredMixin,UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('alumnos:alumnos')
    def get_success_url(self):
        return reverse_lazy('alumnos:editar',args=[self.object.id]) +'?ok'

class AlumnoUpdateGestor(StaffRequiredMixin,UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('alumnos:misAlumnos')
    def get_success_url(self):
        return reverse_lazy('alumnos:editarMiAlumno',args=[self.object.id]) +'?ok'

class AlumnoGestorCreate(AuthenticatedRequiredMixin,CreateView):

    model = Alumno_Gestor
    form_class = AlumnoGestorForm
    second_form_class = AlumnoForm
    success_url = reverse_lazy('alumnos:misAlumnos')

    def get_context_data(self,**kwargs):
        context = super(AlumnoGestorCreate,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            alumno_gestor = form.save(commit=False)
            alumno_gestor.alumno = form2.save()
            alumno_gestor.gestor = Gestor.objects.get(pk=request.user.persona.id) 
            alumno_gestor.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))

class AlumnoGestorListView(ListView):
    model = Alumno_Gestor
    paginate_by = 3    

    def get_queryset(self):
        return Alumno_Gestor.objects.filter(gestor=self.request.user.persona.id)

class AlumnoTutorListView(ListView):
    model = Alumno
    paginate_by = 3    

    def get_queryset(self):
        return Alumno.objects.filter(tutor=self.request.user.persona.id)

