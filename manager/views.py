# Create your views here.
from django.shortcuts import render,redirect
from project.models import Project,MileStone,Requirements
from manager.forms import AddMileStone
def manage(request):
    if request.session['selected_project']:
        pj = Project.objects.get(id = request.session['selected_project_id'])
        milestones = MileStone.objects.filter(project = pj)
        for m in milestones:
            m.requirements = m.requirements_set.all()
        if request.method == "POST":
            form = AddMileStone(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                end_date = form.cleaned_data['end_date']
                start_date = form.cleaned_data['start_date']
                MileStone(project = pj, name = name, description = description, start_date = start_date, end_date = end_date).save()
                notify = True
                message = "MileStone Created"


        else:
            form = AddMileStone()
    return render(request, "manage/manage.html", locals())