# Generated by Django 2.1.2 on 2018-10-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_mascota_vacuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='blog.Vacuna'),
        ),
    ]
