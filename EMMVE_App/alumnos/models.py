from django.db import models
from ckeditor.fields import RichTextField
from registration.models import Persona,Gestor,Docente

# Create your models here.

class Alumno(models.Model):

    MASCULINO = 'M'
    FEMENINO = 'F'
    GENERO_SELECCION = (
    (MASCULINO, 'Másculino'),
    (FEMENINO, 'Femenino'),
    )

    URIZ_PI = 'PI'
    JOAKIN_LIZARRAGA = 'JL'
    CENTRO_ESTUDIOS_SELECCION = (
        (URIZ_PI, 'HERMANAS URIZ PI'),
        (JOAKIN_LIZARRAGA, 'JOAKIN LIZARRAGA'),
    )


    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    primerApellido = models.CharField(max_length=50,verbose_name='Primer apellido')
    segundoApellido = models.CharField(max_length=50,verbose_name='Segundo apellido')
    gestor = models.ManyToManyField(Gestor,through='Alumno_Gestor')
    tutor = models.ForeignKey(Docente, blank=True,null=True, on_delete=models.PROTECT)
    fechaNacimiento = models.DateField()
    avatar = models.ImageField(verbose_name='Imagen', upload_to="alumnos")
    genero = models.CharField(null=True,max_length=1,choices=GENERO_SELECCION,default=MASCULINO) 
    centroEstudios = models.CharField(null=True,blank=True,max_length=2,choices=CENTRO_ESTUDIOS_SELECCION,default=URIZ_PI,verbose_name='Centro escolar')
    activo = models.BooleanField(default=False,null=True,verbose_name='Activo')
    empadronado = models.BooleanField(null=True,verbose_name='Empadronado en el valle de Egüés')
    autorizaImagen = models.BooleanField(null=True,verbose_name='Autoriza uso imágen')
    fichaMedica = models.BooleanField(null=True,verbose_name='Entrega ficha médica')
    content = RichTextField(null=True,blank=True,default='Conocimientos musicales previos',verbose_name='Conocimientos musicales previos')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['nombre','primerApellido','segundoApellido']
        unique_together = ('nombre', 'primerApellido','segundoApellido','fechaNacimiento')
    
    def __str__(self):
        return '{} {} {}'.format(self.nombre,self.primerApellido,self.segundoApellido)


class Alumno_Gestor(models.Model):
    gestor = models.ForeignKey(Gestor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50,verbose_name='Rol del Gestor respecto del Alumno')
    esGestor = models.BooleanField(null=True,verbose_name='Gestiona trámites del alumno')
    esPagador = models.BooleanField(null=True,verbose_name='Paga recibos del alumno')
    recibeNotificaciones = models.BooleanField(null=True,verbose_name='Recibe las notificaciones relativas al alumno')
    domicilioHabitual = models.BooleanField(null=True,verbose_name='Su domicilio es el habitual del alumno')
    
    class Meta:
        verbose_name = "Gestor del Alumno"
        verbose_name_plural = "Gestores del Alumno"
        ordering = ['esGestor','alumno','rol']
    
    def __str__(self):
        return 'Contacto: {} > Alumno : {}  > Rol: {}'.format(str(self.gestor),str(self.alumno),self.rol)