from .forms import UserCreationFormWithEmail,GestorForm,DocenteForm,UserCreationGestorForm,AdministrativoForm,ADM_DocenteForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Persona,Gestor,Docente
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

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    second_form_class = UserCreationGestorForm 
    def get_context_data(self,**kwargs):
        context = super(SignUpView,self).get_context_data(**kwargs)
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
            persona_user = form2.save(commit=False) 
            user = form.save()            
            persona_user.user_id = user.id
            persona_user.save()
            return redirect(reverse_lazy('login') + '?register')
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))

    # Se devuelve una cadena con ?register  en el GET para filtrar los registros realizados correctamente.
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    # Sobreescribimos los widget que tiene el form por defecto para hacerlo mas bonito.
    def get_form(self,form_class=None):
        form = super(SignUpView,self).get_form()
        # Se modifica los widget por defecto del formulario de la clase superior.
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Confirmar contraseña'})
        return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = GestorForm  # Le indico un form class que luego se adapta al adecuado en función al perfil de usuario.  
    success_url = reverse_lazy('profile')
    template_name = 'registration/persona_form.html'    

    def get_object(self):
        persona = Persona.objects.get(user_id=self.request.user.id)
        print (persona.tipoPerfil)
        if persona.tipoPerfil == 'GES':
            print('Devuelvo un objeto tipo Gestor')
            self.form_class = GestorForm
            return Gestor.objects.get(user_id=self.request.user.id)
        elif persona.tipoPerfil == 'DOC':
            print('Devuelvo un objeto tipo Docente')
            self.form_class = DocenteForm
            return Docente.objects.get(user_id=self.request.user.id)
        elif persona.tipoPerfil == 'ADM':
            print('Devuelvo un objeto tipo Administración')
            self.form_class = AdministrativoForm
            return persona

class docenteListView(ListView):
    model = Docente
    paginate_by = 3
    def get_queryset(self):
        return Docente.objects.filter(tipoPerfil='DOC',activo=True)

class docenteCreate(StaffRequiredMixin,CreateView):
    model = Docente
    form_class = ADM_DocenteForm
    success_url = reverse_lazy('docentes')
 

class docenteUpdate(StaffRequiredMixin,UpdateView):
    model = Docente
    form_class = ADM_DocenteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('docentes')

    def get_success_url(self):
        return reverse_lazy('docentesEditar',args=[self.object.id]) +'?ok'

