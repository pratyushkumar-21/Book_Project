# Generated by Django 2.2.6 on 2021-08-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0013_auto_20210809_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='module1_rating',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='module2_rating',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='module3_rating',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='module4_rating',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='module5_rating',
            field=models.PositiveIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
