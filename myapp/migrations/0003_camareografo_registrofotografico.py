# Generated by Django 5.0.1 on 2024-02-14 23:16

import django.db.models.deletion
import myapp.paths
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_autor_librodigital'),
    ]

    operations = [
        migrations.CreateModel(
            name='camareografo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'El Camareografo',
                'verbose_name_plural': 'Los Camareografos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RegistroFotografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_descripcion', models.TextField(blank=True, null=True)),
                ('foto_orientacion', models.CharField(blank=True, default='-', max_length=255, null=True)),
                ('foto_imagen', models.ImageField(blank=True, max_length=500, null=True, upload_to=myapp.paths.get_registro_fotografico_path)),
                ('id_camareografo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.camareografo')),
            ],
            options={
                'verbose_name': 'Foto - Registro fotografico',
                'verbose_name_plural': 'Fotos - Registros fotograficos',
                'ordering': ['-id'],
            },
        ),
    ]