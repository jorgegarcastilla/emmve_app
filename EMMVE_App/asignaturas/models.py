from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Asignatura(models.Model):

	NIVEL_I = 'NI INICIACION'
	NIVEL_II = 'NII STANDARD'
	NIVEL_II_REFORZADO = 'NII REFORZADO'
	NIVEL_II_ACCESO = 'NII ACCESO'
	NIVEL_III = 'NIII'
	MANTENIMIENTO = 'MANTENIMIENTO'
	AGRUPACION = 'AGRUPACION'
	NIVEL_SELECCION = (
		(NIVEL_I, 'Nivel I'),
		(NIVEL_II, 'Nivel II'),
		(NIVEL_II_REFORZADO, 'Nivel II reforzado'),
		(NIVEL_II_ACCESO, 'Nivel II Acceso'),
		(NIVEL_III, 'Nivel III'),
		(MANTENIMIENTO, 'Mantenimiento'),
		(AGRUPACION, 'Sólo agrupación'),
	)
	CURSO_PRIMERO = '1º'
	CURSO_SEGUNDO = '2º'
	CURSO_TERCERO = '3º'
	CURSO_CUARTO = '4º'
	CURSO_QUINTO = '5º'
	CURSO_SEXTO = '6º'
	CURSO_UNICO = 'NA'
	CURSO_SELECCION = (
		(CURSO_PRIMERO, 'Primero'),
		(CURSO_SEGUNDO, 'Segundo'),
		(CURSO_TERCERO, 'Tercero'),
		(CURSO_CUARTO, 'Cuarto'),
		(CURSO_QUINTO, 'Quinto'),
		(CURSO_QUINTO, 'Sexto'),
		(CURSO_UNICO, 'No Aplica'),
	)  
	nombre = models.CharField(max_length=100,verbose_name='Nombre')
	image = models.ImageField(null=True,blank=True,verbose_name='Imagen', upload_to="asignaturas")
	nivel = models.CharField(
		max_length=13,
		choices=NIVEL_SELECCION,
		default=NIVEL_I,
	)
	curso = models.CharField(
		max_length=25,
		choices=CURSO_SELECCION,
		default=CURSO_PRIMERO,
	)
	sesionesSemanales = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],verbose_name='Sesiones semanales')
	duracion = models.IntegerField(validators=[MinValueValidator(15),MaxValueValidator(90)],verbose_name='Duración de la sesión') #Duración en minutos de cada sesión de la asignatura.
	aforoMaximo = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],verbose_name='Aforo máximo')
	aforoMinimo = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)],verbose_name='Aforo mínimo')
	edadMinima = models.IntegerField(validators=[MinValueValidator(4),MaxValueValidator(99)],verbose_name='Edad mínima')
	edadMaxima = models.IntegerField(validators=[MinValueValidator(4),MaxValueValidator(99)],verbose_name='Edad máxima')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de edición')

	class Meta:
		verbose_name = "asignatura"
		verbose_name_plural = "asignaturas"
		ordering = ['nombre']

	def __str__(self):
		return 'Asignatura: {} , Nivel: {} , Curso: {}'.format(self.nombre,self.nivel,self.curso)