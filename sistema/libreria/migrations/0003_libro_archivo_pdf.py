# Generated by Django 4.2 on 2023-07-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_rename_description_libro_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='archivo_pdf',
            field=models.FileField(null=True, upload_to='pdfs/', verbose_name='PDF del Libro'),
        ),
    ]
