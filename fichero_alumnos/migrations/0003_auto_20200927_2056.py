# Generated by Django 3.1.1 on 2020-09-27 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichero_alumnos', '0002_auto_20200927_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]