# Generated by Django 2.2.6 on 2020-01-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0007_auto_20200126_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester1subject',
            name='teacher',
            field=models.CharField(default='pratyush', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester2subject',
            name='teacher',
            field=models.CharField(default='pratyush', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester3subject',
            name='teacher',
            field=models.CharField(default='pratyush', max_length=30),
            preserve_default=False,
        ),
    ]
