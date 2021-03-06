# Generated by Django 4.0.4 on 2022-07-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0008_producto_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCompras',
            fields=[
                ('idCompra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo Compra')),
                ('Usuario', models.CharField(max_length=200, verbose_name='Usuario')),
                ('Productos', models.CharField(max_length=200, verbose_name='Productos Comprados')),
                ('valTotal', models.IntegerField(verbose_name='Valor Total')),
                ('fechaCompra', models.DateField(auto_now_add=True, verbose_name='Fecha Compra')),
            ],
        ),
    ]
