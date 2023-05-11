# Generated by Django 3.1.7 on 2021-07-27 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20210727_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='encuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'encuesta',
                'verbose_name_plural': 'encuestas',
                'db_table': 'encuesta',
            },
        ),
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleccion', models.CharField(max_length=1)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.empleado')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.encuesta')),
            ],
            options={
                'verbose_name': 'respuesta',
                'verbose_name_plural': 'respuestas',
                'db_table': 'respuesta',
            },
        ),
    ]
