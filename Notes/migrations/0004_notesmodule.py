# Generated by Django 2.2.6 on 2020-01-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_auto_20200122_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotesModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.PositiveIntegerField()),
            ],
        ),
    ]
