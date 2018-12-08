# Generated by Django 2.1.3 on 2018-12-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poblacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('codigoPostal', models.CharField(max_length=5, verbose_name='C.P')),
                ('provincia', models.CharField(max_length=25, verbose_name='Provincia')),
                ('comunidadAutonoma', models.CharField(max_length=30, verbose_name='C.A')),
                ('avatar', models.ImageField(upload_to='Poblaciones', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Población',
                'verbose_name_plural': 'Poblaciones',
                'ordering': ['comunidadAutonoma', 'provincia', 'nombre', 'codigoPostal'],
            },
        ),
    ]
