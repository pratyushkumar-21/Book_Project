from django.urls import path
from Notes import views


urlpatterns = [

    path('', views.notes_home),
    path('notes_branch/<int:sem>', views.notes_branch),                          #url for listing branch
    path('subject_list/<int:sem>', views.subject_list),                          # url for sem1 and sem2 subject list
    path('subject_list/<int:sem>/<branch>/',views.subject_list),                  # url for sem3 to sem8 subject list
    path('notes_list/<int:sem>/<subject>/', views.notes_list),                    # url for sem1 and sem2 notes list
    path('rates/<int:id>/', views.rates),

    ]
