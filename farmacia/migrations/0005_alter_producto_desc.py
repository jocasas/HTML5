# Generated by Django 4.0.4 on 2022-05-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0004_rename_productosmedicamentos_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='descripcion'),
        ),
    ]
