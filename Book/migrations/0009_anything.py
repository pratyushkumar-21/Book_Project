# Generated by Django 2.2.6 on 2019-10-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20191016_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anything',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
