from django.db import models
from poblaciones.models import Poblacion
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Persona(models.Model):

    DOCENTE = 'DOC'
    GESTOR_ALUMNO = 'GES'
    ADMINISTRATIVO = 'ADM'
    PERFIL_SELECCION = (
        (DOCENTE, 'Docente'),
        (GESTOR_ALUMNO, 'Gestor'),
        (ADMINISTRATIVO, 'Administrativo'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(null=True,blank=True,verbose_name='Avatar',upload_to = 'Personas')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    primerApellido = models.CharField(max_length=50,verbose_name='Primer apellido')
    segundoApellido = models.CharField(max_length=50,verbose_name='Segundo apellido')
    dni = models.CharField(max_length=9,verbose_name='D.N.I.')
    telefonoPrincipal = models.CharField(max_length=9,verbose_name='Teléfono principal')
    telefonoSecundario = models.CharField(blank=True,max_length=9,verbose_name='Teléfono secundario')
    direccion = models.CharField(max_length=100,verbose_name='Dirección postal')
    poblacion = models.ForeignKey(Poblacion, null=True, blank = True,on_delete=models.SET_NULL,verbose_name='Población')
    tipoPerfil = models.CharField(max_length=3,choices=PERFIL_SELECCION,verbose_name='Perfil de usuario',default=GESTOR_ALUMNO)
    activo = models.BooleanField(default=True,verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')    

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ["nombre","primerApellido","segundoApellido"]

    def __str__(self):
        return self.nombre

class Gestor(Persona):

    #Atributos para el caso de gestor de alumnos
    numeroCC = models.CharField(blank=True,max_length=20,verbose_name='Número CC')
    iban = models.CharField(blank=True,max_length=4,verbose_name='IBAN')
    swift = models.CharField(blank=True,max_length=11,verbose_name='SWIFT')
    rentaBasica = models.BooleanField(null=True,verbose_name='Renta Básica')
    familiaNumerosa = models.BooleanField(null=True,verbose_name='Familia Numerosa')

    class Meta:
        verbose_name = "Gestor"
        verbose_name_plural = "Gestores"
        ordering = ["nombre","primerApellido","segundoApellido"]

    def __str__(self):
        return self.nombre

class Docente(Persona):

    #Atributos para el caso de docente
    link = models.URLField(null=True,blank=True,verbose_name='Dirección WEB')
    jornada = models.DecimalField(default=100.00,validators=[MinValueValidator(0),MaxValueValidator(100,0)],max_digits=5, decimal_places=2,verbose_name='Jornada')	
    rolDirector = models.BooleanField(null=True,verbose_name='Director')
    rolJefatura = models.BooleanField(null=True,verbose_name='Jefatura')


    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        ordering = ["nombre","primerApellido","segundoApellido"]

    def __str__(self):
        return '{} {} {}'.format(str(self.nombre),str(self.primerApellido),self.segundoApellido)
