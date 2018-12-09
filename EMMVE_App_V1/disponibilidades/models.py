from django.db import models
from registration.models import Docente
from alumnos.models import Alumno
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

#Create your models here.

class Disponibilidad(models.Model):

    LUNES = 'L'
    MARTES = 'M'
    MIERCOLES = 'X'
    JUEVES = 'J'
    VIERNES = 'V'
    DIA_SEMANA_SELECCION = (
    (LUNES, 'Lunes'),
    (MARTES, 'Martes'),
    (MIERCOLES, 'Miércoles'),
    (JUEVES, 'Jueves'),
    (VIERNES, 'Viernes'),
    ) 

    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    diaSemana = models.CharField(
    max_length=1,
    choices=DIA_SEMANA_SELECCION,
    default=LUNES,
    )
    cursoAcademico=models.IntegerField(default=datetime.now().year,validators=[MinValueValidator(2018)])
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "Disponibilidad"
        verbose_name_plural = "Disponibilidades"
        ordering = ['cursoAcademico','diaSemana','horaInicio']

    def __str__(self):
        return 'Dia: {} > HoraInicio: {} > HoraFin: {} Curso: {}'.format(self.diaSemana,self.horaInicio,self.horaFin,self.cursoAcademico)

class DisponibilidadDocente(Disponibilidad):

	docente=models.ForeignKey(Docente, on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return 'Docente : {}  > Disponibilidad: {} '.format(str(self.docente),super.__name__)

class DisponibilidadAlumno(Disponibilidad):

	alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)

	def __str__(self):
		return 'Alumno : {}  > Disponibilidad: {} '.format(str(self.alumno),super.__name__)
