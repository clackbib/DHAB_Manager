# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms

from project.models import Project, MileStone, Requirements, Assignment
from manager.forms import AddMileStone, EditMileStone, AssignmentForm


@login_required(login_url="login.views.connect")
def manage(request):
    if request.session['selected_project']:
        pj = Project.objects.get(id=request.session['selected_project_id'])
        milestones = MileStone.objects.filter(project=pj)
        requirements = Requirements.objects.filter(project=pj)
        assignment_list = Assignment.objects.filter(project=pj)
        if request.method == "POST":
            form = AddMileStone(request.POST)
            form2 = AssignmentForm(request.POST)
            notify = True
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                end_date = form.cleaned_data['end_date']
                start_date = form.cleaned_data['start_date']
                MileStone(project=pj, name=name, description=description, start_date=start_date,
                          end_date=end_date).save()
                message = "MileStone Created"
                return redirect("manager.views.manage")
            else:
                message = "Invalid Milestone Information"
            if form2.is_valid():
                form_requirement = form2.cleaned_data['requirement']
                form_profile = form2.cleaned_data['profile']
                form_role = form2.cleaned_data['role']
                form_task = form2.cleaned_data['task']
                Assignment(requirement=form_requirement, profile=form_profile, role=form_role, task=form_task,
                           project=pj).save()
                return redirect("manager.views.manage")

            else:
                message = "Invalid Assignment Information"
        else:
            form = AddMileStone()
            form2 = AssignmentForm()
    return render(request, "manage/manage.html", locals())


@login_required(login_url="login.views.connect")
def delete_assoc(request, id):
    r = get_object_or_404(Requirements, id=id)
    r.milestone = None
    r.save()
    return redirect("manager.views.manage")


def edit_milestone(request, id):
    project = Project.objects.get(id=request.session['selected_project_id'])
    milestone = get_object_or_404(MileStone, id=id, project=project)
    if request.method == "POST":
        form = EditMileStone(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
    else:
        form = EditMileStone(instance=milestone)
        form.fields['start_date'] = forms.DateField(initial=milestone.start_date,
                                                    widget=forms.TextInput(attrs={'class': 'jquery_date'}))
        form.fields['end_date'] = forms.DateField(initial=milestone.end_date,
                                                  widget=forms.TextInput(attrs={'class': 'jquery_date'}))
    return render(request, "manage/edit_milestone.html", locals())


@login_required(login_url="login.views.connect")
def delete_milestone(request, id):
    ms = get_object_or_404(MileStone, id=id)
    ms.delete()
    return redirect("manager.views.manage")