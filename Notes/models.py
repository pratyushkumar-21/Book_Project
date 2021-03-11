from django.db import models

# Create your models here.

# model for semester
class NotesSemester(models.Model):
    semester    =  models.PositiveIntegerField()


# model for branch
class NotesBranch(models.Model):
    branch      =  models.CharField(max_length = 20)


# model for module
class NotesModule(models.Model):
    module      =  models.PositiveIntegerField()


# model for 1st semester subject
class Semester1Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_1_Notes')

# model for 2nd semester subject
class Semester2Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_2_Notes')

# model for 3rd semester subject
class Semester3Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_3_Notes')

# model for 4rd semester subject
class Semester4Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_4_Notes')


# model for 5rd semester subject
class Semester5Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_5_Notes')


# model for 6rd semester subject
class Semester6Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_6_Notes')


# model for 7rd semester subject
class Semester7Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_7_Notes')


# model for 8rd semester subject
class Semester8Subject(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    module      =  models.ForeignKey(NotesModule,on_delete=models.CASCADE)
    teacher     =  models.CharField(max_length = 30)
    file        =  models.FileField(upload_to='Semester_8_Notes')
