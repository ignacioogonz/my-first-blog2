# Generated by Django 2.1.2 on 2018-10-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_datos_personales'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_personales',
            name='cosa',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datos_personales',
            name='opt',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
    ]