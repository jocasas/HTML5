# Generated by Django 4.0.4 on 2022-07-11 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0014_historialcompras_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcompras',
            name='fechallega',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]