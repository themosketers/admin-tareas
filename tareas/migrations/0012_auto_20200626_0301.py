# Generated by Django 3.0.5 on 2020-06-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0011_auto_20200625_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupoactividad',
            options={},
        ),
        migrations.AddField(
            model_name='actividad',
            name='comentarios',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
