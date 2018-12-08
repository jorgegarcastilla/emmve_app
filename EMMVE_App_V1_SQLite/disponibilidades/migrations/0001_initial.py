# Generated by Django 2.1.3 on 2018-12-07 18:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_auto_20181207_1949'),
        ('alumnos', '0003_auto_20181207_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('diaSemana', models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('X', 'Miércoles'), ('J', 'Jueves'), ('V', 'Viernes')], default='L', max_length=1)),
                ('cursoAcademico', models.IntegerField(default=2018, validators=[django.core.validators.MinValueValidator(2018)])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='DisponibilidadAlumno',
            fields=[
                ('disponibilidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disponibilidades.Disponibilidad')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
            ],
            bases=('disponibilidades.disponibilidad',),
        ),
        migrations.CreateModel(
            name='DisponibilidadDocente',
            fields=[
                ('disponibilidad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disponibilidades.Disponibilidad')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Docente')),
            ],
            bases=('disponibilidades.disponibilidad',),
        ),
    ]
