# Generated by Django 4.0.4 on 2022-05-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripEspecifica',
            field=models.CharField(default=0, max_length=200, verbose_name='DescripEspecifica'),
            preserve_default=False,
        ),
    ]
