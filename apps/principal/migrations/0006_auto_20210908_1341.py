# Generated by Django 3.1.7 on 2021-09-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20210902_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='cate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='dominio',
            field=models.IntegerField(null=True),
        ),
    ]
