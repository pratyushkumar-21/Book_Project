# Generated by Django 2.2.6 on 2020-01-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='module',
            field=models.PositiveIntegerField(default=0),
        ),
    ]