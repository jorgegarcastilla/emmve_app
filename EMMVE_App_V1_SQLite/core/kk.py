
# class DisponibilidadDocente(Disponibilidad):

# 	docente=models.ForeignKey(Persona, on_delete=models.CASCADE)
	
# 	def __str__(self):
# 		return 'Docente : {}  > Disponibilidad: {} '.format(str(self.docente),str(super.__name__))

# class DisponibilidadAlumno(Disponibilidad):

# 	alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
	
# 	def __str__(self):
# 		return 'Alumno : {}  > Disponibilidad: {} '.format(str(self.alumno),str(super.__name__))

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
# 	docente=models.ForeignKey(Persona, null=True, on_delete=models.PROTECT)	
# 	aula=models.ForeignKey(Aula, null=True, on_delete=models.PROTECT)
# 	def __str__(self):
# 		return 'Docente : {}  > Disponibilidad: {}  > Asignatura: {} > Aula: {}'.format(str(self.docente),str(super.__name__),str(self.asignatura),str(self.aula)) """

# """ class Matricula(models.Model):
# 	alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
# 	cursoAcademico=models.IntegerField(validators=[MinValueValidator(2018),MaxValueValidator(2118)])
# 	activa = models.BooleanField(null=True)
# 	asignatura =models.ManyToManyField(Asignatura)

# 	def __str__(self):
# 		return 'Alumno: {} Curso Académico: {}'.format(str(self.alumno),self.cursoAcademico) """




# """ class Periodo (models.Model)
# class Boletin(models.Model):
# 	matriculaAsignatura = models.ForeignKey(Matricula_Asignatura, null=True,on_delete=models.PROTECT)
# 	TRIMESTRE_1 = '1T'
# 	TRIMESTRE_2 = '2T'
# 	TRIMESTRE_3 = '3T'
# 	PERIODO_SELECCION = (
# 		(TRIMESTRE_1, 'Primer trimestre'),
# 		(TRIMESTRE_2, 'Segundo trimestre'),
# 		(TRIMESTRE_3, 'Tercer trimestre'),
# 	)
# 	periodo = models.CharField(
# 	null=True,
# 	max_length=2,
# 	choices=PERIODO_SELECCION,
# 	default=TRIMESTRE_1,
# 	) 
# 	MUY_BIEN = 'A'
# 	BIEN = 'B'
# 	NORMAL = 'C'
# 	INSUFICIENTE = 'D'
# 	NOTAS_BOLETIN_SELECCION = (
# 		(MUY_BIEN, 'Muy Bien'),
# 		(BIEN, 'Bien'),
# 		(NORMAL, 'Normal'),
# 		(INSUFICIENTE, 'Insuficiente'),
# 	)
# 	estudio = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	actitud = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	faltas=models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	requisitoConciertos = models.BooleanField(null=True)
# 	observaciones = models.TextField(blank =True,max_length=255)

# 	def __str__(self):
# 		return '{} > Periodo: {}'.format(str(self.matriculaAsignatura),self.periodo)

# class BoletinIniciacion(models.Model):
# 	matriculaAsignatura = models.ForeignKey(Matricula_Asignatura, null=True,on_delete=models.PROTECT)
# 	TRIMESTRE_1 = '1T'
# 	TRIMESTRE_2 = '2T'
# 	TRIMESTRE_3 = '3T'
# 	PERIODO_SELECCION = (
# 		(TRIMESTRE_1, 'Primer trimestre'),
# 		(TRIMESTRE_2, 'Segundo trimestre'),
# 		(TRIMESTRE_3, 'Tercer trimestre'),
# 	)
# 	periodo = models.CharField(
# 	null=True,
# 	max_length=2,
# 	choices=PERIODO_SELECCION,
# 	default=TRIMESTRE_1,
# 	) 
# 	MUY_BIEN = 'A'
# 	BIEN = 'B'
# 	NORMAL = 'C'
# 	INSUFICIENTE = 'D'
# 	NOTAS_BOLETIN_SELECCION = (
# 		(MUY_BIEN, 'Muy Bien'),
# 		(BIEN, 'Bien'),
# 		(NORMAL, 'Normal'),
# 		(INSUFICIENTE, 'Insuficiente'),
# 	)
# 	educacionAuditiva = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	audicionMusical = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	)
# 	expresionVocal = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	expresionInstrumental = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	expresionRitmica = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	)
# 	expresionCorporal = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	actitud = models.CharField(
# 	null=True,
# 	max_length=1,
# 	choices=NOTAS_BOLETIN_SELECCION,
# 	default=INSUFICIENTE,
# 	) 
# 	faltas=models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	observaciones = models.TextField(blank=True,max_length=255)

# 	def __str__(self):
# 		return '{} > Periodo: {}'.format(str(self.matriculaAsignatura),self.periodo)

# class ActividadAcademica(models.Model):
# 	matriculaAsignatura = models.ForeignKey(Matricula_Asignatura, on_delete=models.PROTECT)
# 	clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return '{} > {}'.format(str(self.matriculaAsignatura),str(self.clase))

# class DocenteAsignatura(models.Model):
# 	docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
# 	asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return '{} > {}'.format(str(self.docente),str(self.asignatura))


# class AulaAsignatura(models.Model):
# 	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
# 	asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return '{} > {}'.format(str(self.aula),str(self.asignatura))

# class EvaluacionContinua(models.Model):
# 	actividadAcademica = models.ForeignKey(ActividadAcademica, on_delete=models.CASCADE)
# 	observaciones = models.TextField(blank=True,max_length=255)
# 	asistencia = models.BooleanField(null=True)

# 	def __str__(self):
# 		return '{}'.format(str(self.actividadAcademica))

# class Evento(models.Model):
# 	nombre = models.CharField(null=True,max_length=50)
# 	fechaInicio = models.DateTimeField()
# 	fechaFin = models.DateTimeField()
# 	descripcion = models.TextField(blank=True,max_length=255)

# 	def __str__(self):
# 		return 'Mnemónico: {}'.format(self.nombre)

# class ListaEspera(models.Model):
# 	alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
# 	asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
# 	ordenEnLista=models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	ordenPreferencia=models.IntegerField(default=0,validators=[MinValueValidator(0)])
# 	numeroSorteo=models.IntegerField(default=0,validators=[MinValueValidator(0)])

# 	def __str__(self):
# 		return '{} > {} > Posicion en lista: {} > Numero para sorteo: {}'.format(str(self.alumno),str(self.asignatura),str(self.ordenEnLista),str(self.numeroSorteo))

# class Pago(models.Model):
# 	matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
# 	importe = models.FloatField()
# 	concepto = models.CharField(max_length=50)
# 	fechaInicio = models.DateField()
# 	fechaFin = models.DateField()
# 	pagado = models.BooleanField(null=True)
# 	descuento = models.BooleanField(null=True)

# 	def __str__(self):
# 		return '{} > Concepto: {} > Cantidad: {}'.format(str(self.matricula),self.concepto,self.importe)

# class Parametro(models.Model):
# 	clave = models.CharField(max_length=50)
# 	valor = models.CharField(max_length=10)
# 	INTEGER = 'INT'
# 	REAL = 'REAL'
# 	BOOLEANO = 'BOOL'
# 	TIPO_PARAMETRO_SELECCION = (
# 		(INTEGER, 'Entero'),
# 		(REAL, 'Real'),
# 		(BOOLEANO, 'Booleano'),
# 	)
# 	tipo = models.CharField(
# 		max_length=4,
# 		choices=TIPO_PARAMETRO_SELECCION,
# 		default=INTEGER,
# 	) 
# 	def __str__(self):
# 		return 'Clave: {}'.format(self.clave)

# #Tendrias que tener una entidad por cada tipo de registro para que se puedan rellenar directamente desde la aplicación.
# class Registro(models.Model):
# 	alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
# 	fecha = models.DateTimeField()
# 	codigoDocumento = models.CharField(max_length=50)
# 	PREINSCRIPCION = 'PRE'
# 	RENUNCIA = 'REN'
# 	MATRICULA = 'MAT'
# 	BANCO = 'BCO'
# 	BAJA = 'BJA'
# 	CAMBIO = 'CBO'
# 	DESCUENTO = 'DTO'
# 	CUENTA = 'CTA'
# 	QUEJA = 'QJA'
# 	FICHA_MEDICA = 'MED'
# 	TIPO_REGISTRO_SELECCION = (
# 		(PREINSCRIPCION, 'Preinscripción'),
# 		(RENUNCIA, 'Renuncia'),
# 		(MATRICULA, 'Matricula'),
# 		(BANCO, 'Permiso cobro bancario'),
# 		(BAJA, 'Baja'),
# 		(CAMBIO, 'Solicitud de cambio horario'),
# 		(DESCUENTO, 'Descuento'),
# 		(CUENTA, 'Cuenta de cobro'),
# 		(QUEJA, 'Queja'),
# 		(FICHA_MEDICA, 'Ficha médica'),
# 	)
# 	tipo = models.CharField(
# 		max_length=3,
# 		choices=TIPO_REGISTRO_SELECCION,
# 		default=PREINSCRIPCION,
# 	)

# 	def __str__(self):
# 		return '{} > Tipo: {} > Archivo: {}'.format(str(self.alumno),self.tipo,self.codigoDocumento)

# class Reserva(models.Model):
# 	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
# 	docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
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
# 	cursoAcademico=models.IntegerField(validators=[MinValueValidator(2018),MaxValueValidator(2118)])
# 	motivo = models.CharField(max_length=50)

	
# 	def __str__(self):
# 		return '{} > Dia: {} Horario: {}-{} > {}'.format(str(self.aula),self.diaSemana,self.horaInicio,self.horaFin,str(self.docente))	


# class AccionPendienteDocente(models.Model):

# 	docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
# 	fechaInicio = models.DateTimeField()
# 	fechaFin = models.DateTimeField()
# 	finalizada = models.BooleanField(null=True)
# 	descripcionBreve = models.CharField(default='',blank =True,max_length=50)
# 	descripcion = models.TextField(blank=True,max_length=255)

# 	def __str__(self):
# 		return 'Docente: {} > Acción: {} > {}'.format(str(self.docente),self.descripcionBreve,self.descripcion)	

# class AccionPendienteAlumno(models.Model):

# 	alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
# 	fechaInicio = models.DateTimeField()
# 	fechaFin = models.DateTimeField()
# 	finalizada = models.BooleanField(null=True)
# 	descripcionBreve = models.CharField(default='',blank =True,max_length=50)
# 	descripcion = models.TextField(blank=True,max_length=255)

# 	def __str__(self):
# 		return 'Alumno: {} > Acción: {} > {}'.format(str(self.alumno),self.descripcionBreve,self.descripcion)	

# class AccionPendienteAdministracion(models.Model):

# 	fechaInicio = models.DateTimeField()
# 	fechaFin = models.DateTimeField()
# 	finalizada = models.BooleanField(null=True)
# 	descripcionBreve = models.CharField(default='',blank =True,max_length=50)
# 	descripcion = models.TextField(blank=True,max_length=255)
# 	# Según la acción la aplicación incluirá uno u otro texto
# 	# Si es preinscripción : Accion : Revisar Preinscripción.
# 	# Se incluye en el texto, el nombre y apellidos del candidato.
# 	# Hay una opción para administración : Revisar candidatura a partir del nombre y apellidos
# 	# le sale toda la información del alumno, su gestor y listas a las que oposita

# 	def __str__(self):
# 		return 'ACCION: {} > {}'.format(self.descripcionBreve,self.descripcion)	