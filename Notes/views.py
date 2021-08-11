from django.shortcuts import render
from django.db.models import Q
from Notes import models
from django.contrib.auth.decorators import login_required


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
        search = request.POST['search']
        module_list = models.Notes.objects.filter(subject__contains = search)
        return render(request,'Notes/subject_list.html', {'module_list':module_list})

    module_list = models.Notes.objects.filter(subject__contains =subject, semester__exact =sem)
    module1_rating,module2_rating,module3_rating,module4_rating,module5_rating = 0,0,0,0,0
    for module in module_list:
        notes_id = module.id
        rating = models.Rating.objects.filter(notes = notes_id)
        if len(rating) != 0:
            for i in rating:
                module1_rating += i.module1_rating
                module2_rating += i.module2_rating
                module3_rating += i.module3_rating
                module4_rating += i.module4_rating
                module5_rating += i.module5_rating
            module.module1_rating = round(module1_rating / len(rating), 1)
            module.module2_rating = round(module2_rating / len(rating), 1)
            module.module3_rating = round(module3_rating / len(rating), 1)
            module.module4_rating = round(module4_rating / len(rating), 1)
            module.module5_rating = round(module5_rating / len(rating), 1)
            module1_rating,module2_rating,module3_rating,module4_rating,module5_rating = 0,0,0,0,0

    return render(request,'Notes/notes_list.html',{'module_list':module_list})

# views for presenting list of subject
def subject_list(request,sem,branch = None):
    # for searching :-- function will be implemented in future
    if request.method == 'POST':
        return render(request,'Notes/subject_list.html')
    if branch:
        subject_list = []
        subject_lists = models.Notes.objects.filter(semester__exact = sem)
        for subject in subject_lists:
            if subject.branch.branch.lower() == branch.lower():
                subject_list.append(subject)
    else:
        subject_list = models.Notes.objects.filter(semester__exact = sem)

    subject_set = set()
    for subject in subject_list:
        subject = subject.subject.upper()
        subject_set.add(subject)
    return render(request,'Notes/subject_list.html',{'subject_list':subject_set,'sem':sem})

@login_required 
def rates(request, id):
    if request.method == "POST":
        data = request.POST
        module1 = data['module1'][0]
        module2 = data['module2'][0]
        module3 = data['module3'][0]
        module4 = data['module4'][0]
        module5 = data['module5'][0]
        notes = models.Notes.objects.get(id= id)
        rate = models.Rating(user= request.user, notes= notes, module1_rating= module1, module2_rating= module2, module3_rating= module3, module4_rating= module4, module5_rating= module5)
        rate.save()

        return render(request, 'Notes/thanks.html')
    return render(request, 'Notes/rates.html')
