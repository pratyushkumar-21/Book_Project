from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for semester
class NotesSemester(models.Model):
    semester    =  models.PositiveIntegerField()

    def __str__(self):
        return str(self.semester)


# model for branch
class NotesBranch(models.Model):
    branch      =  models.CharField(max_length = 20)

    def __str__(self):
        return str(self.branch)


# model for module
class NotesModule(models.Model):
    module      =  models.PositiveIntegerField()

    def __str__(self):
        return str(self.module)

# models for uploading the notes
class Notes(models.Model):
    semester    =  models.ForeignKey(NotesSemester,on_delete=models.CASCADE)
    branch      =  models.ForeignKey(NotesBranch,on_delete=models.CASCADE)
    subject     =  models.CharField(max_length = 30)
    notes_by     =  models.CharField(max_length = 30)
    module1     =  models.FileField(upload_to='Notes', blank= True)
    module2     =  models.FileField(upload_to='Notes', blank= True)
    module3     =  models.FileField(upload_to='Notes', blank= True)
    module4     =  models.FileField(upload_to='Notes', blank= True)
    module5     =  models.FileField(upload_to='Notes', blank= True)
    module1_rating = models.PositiveIntegerField(blank= True)
    module2_rating = models.PositiveIntegerField(blank= True)
    module3_rating = models.PositiveIntegerField(blank= True)
    module4_rating = models.PositiveIntegerField(blank= True)
    module5_rating = models.PositiveIntegerField(blank= True)

    def __str__(self):
        return self.subject


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE)
    module1_rating = models.PositiveIntegerField(blank= True)
    module2_rating = models.PositiveIntegerField(blank= True)
    module3_rating = models.PositiveIntegerField(blank= True)
    module4_rating = models.PositiveIntegerField(blank= True)
    module5_rating = models.PositiveIntegerField(blank= True)
    
