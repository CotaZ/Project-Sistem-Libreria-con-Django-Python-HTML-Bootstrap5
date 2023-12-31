# Generated by Django 4.2 on 2023-07-23 23:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_archivo_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('profesion', models.CharField(choices=[('Ninguna', 'Ninguna'), ('Estudiante', 'Estudiante'), ('Profesional', 'Profesional'), ('Educador', 'Educador')], default='Ninguna', max_length=50)),
                ('rut', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('pais', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=20)),
            ],
        ),
    ]
