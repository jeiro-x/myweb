# Generated by Django 5.0.1 on 2024-02-11 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LibroDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editorial', models.CharField(max_length=255)),
                ('fecha_publicacion', models.DateField()),
                ('formato', models.CharField(max_length=50)),
                ('tamano', models.CharField(max_length=50)),
                ('url_descarga', models.URLField()),
                ('autor_adicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros_digitales', to='myapp.autor')),
            ],
            options={
                'verbose_name': 'Libro Digital',
                'verbose_name_plural': 'Libros Digitales',
            },
        ),
    ]
