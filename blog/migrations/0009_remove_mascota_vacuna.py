# Generated by Django 2.1.2 on 2018-10-30 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_mascota_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='vacuna',
        ),
    ]
