# Generated by Django 2.1.2 on 2018-11-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=22, max_length=200),
            preserve_default=False,
        ),
    ]
