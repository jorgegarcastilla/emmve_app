from django.db import models

# # Create your models here.
# from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# from django.contrib.auth.models import User
from datetime import datetime

# from registration.models import Persona
# from asignaturas.models import Asignatura
# from aula.models import aula
# from alumnos.models import Alumno


# class Aula(models.Model):

# 	nombre = models.CharField(max_length=20)
# 	superficie = models.IntegerField(validators=[MinValueValidator(1)]) # Escalar a 1 decimal.
# 	aforo = models.IntegerField(validators=[MinValueValidator(1)])
# 	aula = models.ForeignKey(aula, null=True, blank = True,on_delete=models.SET_NULL)

# 	def __str__(self):
# 		return 'Aula: {} > aula: {}'.format(self.nombre,self.aula.nombre)
# class Usuario(models.Model):
# 	Nombre = models.TextField(max_length=20)
# 	Contraseña = models.TextField(max_length=20)

# class Humano(models.Model):
# 	Sexo = models.TextField(max_length=1)
# 	Edad = models.IntegerField()
# 	usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE,null=True,blank=True)


# class Profesor(models.Model):
# 	Universidad = models.TextField(max_length=20)
# 	humano = models.OneToOneField(Humano,on_delete=models.CASCADE,null=True,blank=True)


# class TutorLegal(models.Model):
# 	Domicilio = models.TextField(max_length=200)
# 	humano = models.OneToOneField(Humano,on_delete=models.CASCADE,null=True,blank=True)

# class Estudiante(Humano):
# 	Asignatura = models.TextField(max_length=20)
# 	Profesor = models.ManyToManyField(Profesor)
# 	TutorLegal = models.ForeignKey(TutorLegal,on_delete=models.CASCADE)


# class Disponibilidad(models.Model):

# 	LUNES = 'L'
# 	MARTES = 'M'
# 	MIERCOLES = 'X'
# 	JUEVES = 'J'
# 	VIERNES = 'V'
# 	DIA_SEMANA_SELECCION = (
# 		(LUNES, 'Lunes'),
# 		(MARTES, 'Martes'),
# 		(MIERCOLES, 'Miércoles'),
# 		(JUEVES, 'Jueves'),
# 		(VIERNES, 'Viernes'),
# 	) 

# 	horaInicio = models.TimeField()
# 	horaFin = models.TimeField()
# 	diaSemana = models.CharField(
# 		max_length=1,
# 		choices=DIA_SEMANA_SELECCION,
# 		default=LUNES,
# 	)
# 	cursoAcademico=models.IntegerField(default=datetime.now().year,validators=[MinValueValidator(2018)])
# 	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
# 	updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

# 	def __str__(self):
# 		return 'Dia: {} > HoraInicio: {} > HoraFin: {} Curso: {}'.format(self.diaSemana,self.horaInicio,self.horaFin,self.cursoAcademico)

# class Prueba(models.Model):
# 	Herencia = models.OneToOneField(Disponibilidad,on_delete=models.CASCADE)
# 	kk = models.IntegerField()

# class DisponibilidadDocente(Disponibilidad):

# 	docente=models.ForeignKey(Persona, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return 'Docente : {}  > Disponibilidad: {} '.format(str(self.docente),super.__name__)

# class DisponibilidadAlumno(Disponibilidad):

# 	alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return 'Alumno : {}  > Disponibilidad: {} '.format(str(self.alumno),super.__name__)



# class DisponibilidadClase(Disponibilidad):

# 	UNICO ='U' 
# 	A = 'A'
# 	B = 'B'
# 	C = 'C'
# 	GRUPO = (
# 		(UNICO, 'GRUPO ÚNICO'),
# 		(A, 'GRUPO A'),
# 		(B, 'GRUPO B'),
# 		(C, 'GRUPO C'),
# 	)
# 	grupo = models.CharField(
# 		max_length=1,
# 		choices=GRUPO,
# 		default=UNICO,
# 	)
#     asignatura=models.ForeignKey(Asignatura, null=True, on_delete=models.PROTECT)
#     docente=models.ForeignKey(Persona, null=True, on_delete=models.PROTECT)	
#     aula=models.ForeignKey(Aula, null=True, on_delete=models.PROTECT)

# 	def __str__(self):
#         return 'Docente : {}  > Disponibilidad: {}  > Asignatura: {} > Aula: {}'.format(str(self.docente),str(super.__name__),str(self.asignatura),str(self.aula))