# Generated by Django 2.2.6 on 2020-01-25 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0020_auto_20200122_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 25, 23, 47, 2, 607617)),
        ),
    ]