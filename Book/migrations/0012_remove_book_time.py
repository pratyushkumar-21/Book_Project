# Generated by Django 2.2.6 on 2019-10-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_book_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='time',
        ),
    ]
