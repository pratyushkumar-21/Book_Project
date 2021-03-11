from django.shortcuts import render
from django.db.models import Q
from Notes import models


# Create your views here.

# notes home page view
def notes_home(request):
    return render(request,'Notes/notes_home.html')


# views for branch selection
def notes_branch(request,sem):
    return render(request,'Notes/notes_branch.html',{'sem':sem})


# views for presenting list of notes
def notes_list(request,sem,subject,branch = None):
    # for searching :-- function will be implemented in future
    if request.method == 'POST':
        return render(request,'Notes/subject_list.html')

    if (sem == 1):
        module_list = models.Semester1Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break
    elif (sem == 2):
        module_list = models.Semester2Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 3):
        module_list = models.Semester3Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 4):
        module_list = models.Semester4Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 5):
        module_list = models.Semester5Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 6):
        module_list = models.Semester6Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 7):
        module_list = models.Semester7Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    elif (sem == 8):
        module_list = models.Semester8Subject.objects.filter(subject__contains =subject).order_by('module')
        for module in module_list:
            teacher = module.teacher
            break

    return render(request,'Notes/notes_list.html',{'module_list':module_list,'subject':subject,'teacher':teacher})





# views for presenting list of subject
def subject_list(request,sem,branch = None):
    # for searching :-- function will be implemented in future
    if request.method == 'POST':
        return render(request,'Notes/subject_list.html')

    if (sem == 1):
        subject_list = models.Semester1Subject.objects.filter(semester__exact = sem)
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 2):
        subject_list = models.Semester2Subject.objects.filter(semester__exact = sem)
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 3):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester3Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 4):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester4Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 5):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester5Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 6):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester6Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 7):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester7Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    elif (sem == 8):
        branch       = models.NotesBranch.objects.filter(branch__icontains = branch)
        subject_list = models.Semester8Subject.objects.filter(Q(semester__exact = sem),Q(branch__exact = branch[0]))
        subject_set = set()
        for subject in subject_list:
            subject = subject.subject.upper()
            subject_set.add(subject)

    return render(request,'Notes/subject_list.html',{'subject_list':subject_set,'sem':sem})
