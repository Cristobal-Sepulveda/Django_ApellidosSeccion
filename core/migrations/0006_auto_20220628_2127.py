# Generated by Django 3.2.12 on 2022-06-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idCliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.CharField(default=2, max_length=50, verbose_name='correo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut'),
        ),
    ]
