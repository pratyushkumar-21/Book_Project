# Generated by Django 2.2.6 on 2020-01-25 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0021_auto_20200125_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 26, 0, 44, 13, 15858)),
        ),
    ]