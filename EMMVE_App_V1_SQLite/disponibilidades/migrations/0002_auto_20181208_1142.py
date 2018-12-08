# Generated by Django 2.1.3 on 2018-12-08 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disponibilidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disponibilidad',
            options={'ordering': ['cursoAcademico', 'diaSemana', 'horaInicio'], 'verbose_name': 'Disponibilidad', 'verbose_name_plural': 'Disponibilidades'},
        ),
        migrations.AlterField(
            model_name='disponibilidaddocente',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Docente'),
        ),
    ]
