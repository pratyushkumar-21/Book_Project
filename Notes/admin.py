from django.contrib import admin
# from Notes.models import NotesSemester,NotesBranch,NotesModule,Semester1Subject,Semester2Subject
from Notes import models

# Register your models here.

# admin for notes_semester modle
class NotesSemesterAdmin(admin.ModelAdmin):
    list_display   = ['semester']

admin.site.register(models.NotesSemester,NotesSemesterAdmin)


# admin for notes_branch modle
class NotesBranchAdmin(admin.ModelAdmin):
    list_display   = ['branch']

admin.site.register(models.NotesBranch,NotesBranchAdmin)


# admin for notes_module modle
class NotesModuleAdmin(admin.ModelAdmin):
    list_display   = ['module']

admin.site.register(models.NotesModule,NotesModuleAdmin)


# admin for semester_1_subject modle
class Semester1SubjectAdmin(admin.ModelAdmin):
    list_display   =  ['subject','semester','module','teacher','file']

admin.site.register(models.Semester1Subject,Semester1SubjectAdmin)


# admin for semester_2_subject modle
class Semester2SubjectAdmin(admin.ModelAdmin):
    list_display   =  ['subject','semester','module','teacher','file']

admin.site.register(models.Semester2Subject,Semester2SubjectAdmin)


# admin for semester_3_subject modle
class Semester3SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester3Subject,Semester3SubjectAdmin)


# admin for semester_4_subject modle
class Semester4SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester4Subject,Semester4SubjectAdmin)


# admin for semester_5_subject modle
class Semester5SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester5Subject,Semester5SubjectAdmin)


# admin for semester_6_subject modle
class Semester6SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester6Subject,Semester6SubjectAdmin)


# admin for semester_7_subject modle
class Semester7SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester7Subject,Semester7SubjectAdmin)


# admin for semester_8_subject modle
class Semester8SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','semester','branch','module','teacher','file']

admin.site.register(models.Semester8Subject,Semester8SubjectAdmin)
