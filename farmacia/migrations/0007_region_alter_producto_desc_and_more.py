# Generated by Django 4.0.4 on 2022-06-06 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0006_alter_producto_idproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False, verbose_name='IdRegion')),
                ('nomRegion', models.CharField(max_length=40, verbose_name='Nombre region')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='desc',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripEspecifica',
            field=models.CharField(max_length=200, verbose_name='Detalles'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProd',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidades',
            field=models.CharField(max_length=20, verbose_name='Unidad o medida'),
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.IntegerField(primary_key=True, serialize=False, verbose_name='IdComuna')),
                ('nomComuna', models.CharField(max_length=40, verbose_name='Nombre Comuna')),
                ('idREG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.region')),
            ],
        ),
    ]
