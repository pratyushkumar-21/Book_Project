from django.contrib import admin
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

# admin for uploading notes
class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester', 'branch', 'subject', 'notes_by', 'module1', 'module2', 'module3', 'module4', 'module5']

admin.site.register(models.Notes, NotesAdmin)

# admin for notes rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'notes', 'module1_rating', 'module2_rating', 'module3_rating', 'module4_rating', 'module5_rating']

admin.site.register(models.Rating, RatingAdmin)