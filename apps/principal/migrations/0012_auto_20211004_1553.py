# Generated by Django 3.1.7 on 2021-10-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultado',
            name='atencion_clinica',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='contesto',
            field=models.BooleanField(default=False),
        ),
    ]
