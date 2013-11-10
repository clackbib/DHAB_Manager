# Create your views here.
from django.shortcuts import render
from project.models import MileStone,Requirements,Project


def reports(request):
    if request.session['selected_project']:
        pj = Project.objects.get(id = request.session['selected_project_id'])
        milestones = MileStone.objects.filter(project = pj)
        for m in milestones:
            m.requirements = m.requirements_set.all()


    return render(request, "reports/reports.html", locals())