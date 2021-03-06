# Generated by Django 2.2.6 on 2020-01-25 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0005_semester1subject_semester2subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester3Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='Semester_3_Notes')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.NotesBranch')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.NotesModule')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.NotesSemester')),
            ],
        ),
    ]
