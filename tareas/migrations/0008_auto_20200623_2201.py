# Generated by Django 3.0.5 on 2020-06-24 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_auto_20200623_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='grupoactividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.GrupoActividad'),
        ),
    ]