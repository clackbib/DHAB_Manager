# Create your views here.
from django.shortcuts import render,redirect
from project.forms import NewProjectForm, AddRequirementForm, EditRequirement
from project.models import Project, Requirements
from login.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404

@login_required(login_url="login.views.connect")
def add_project(request):
    notify = False
    message = ''
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user = request.user)
            Project(creator=profile, name= form.cleaned_data['name'], description = form.cleaned_data['description']).save();
            notify = True
            return redirect("project.views.projects")
        else:
            notify = True
            message = 'Form invalid'

    else:
        form = NewProjectForm()
    return render(request, "project/add_project.html", locals())

@login_required(login_url="login.views.connect")
def projects(request):
     profile = Profile.objects.get(user = request.user)
     projects = Project.objects.filter(creator = profile)
     request.session['current_user_projects'] = projects
     return render(request, 'project/projects.html', locals())

@login_required(login_url="login.views.connect")
def update_project(request):
    request.session['selected_project_id'] = request.POST['project']
    request.session['selected_project'] = Project.objects.get(id = request.POST['project']).name
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),locals())

@login_required(login_url="login.views.connect")
def requirements(request):


    if request.session['selected_project']:
        pj = Project.objects.get(id = request.session['selected_project_id'])
        requirements =  Requirements.objects.filter(project = pj)
        for r in requirements:
            r.ratio = (r.current_completion/r.size_estimate)*100
        if request.method == 'POST':
            form = AddRequirementForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                size_estimate = form.cleaned_data['size_estimate']
                technique = form.cleaned_data['technique']
                requirement_type = form.cleaned_data['requirement_type']
                end_date = form.cleaned_data['end_date']
                profile = Profile.objects.get(user = request.user)
                req = Requirements(project = pj, creator = profile, name = name, description = description, size_estimate=size_estimate,
                                   technique=technique, requirement_type=requirement_type, end_date=end_date)
                req.save();
                notify = True;
                message = 'Requirement Saved.'
                return redirect("project.views.requirements")
        else:
            form = AddRequirementForm()

    return render(request, 'project/requirements.html', locals())


@login_required(login_url="login.views.connect")
def edit_requirement(request, id):
    project = Project.objects.get(id = request.session['selected_project_id'] )
    req = get_object_or_404(Requirements,id = id, project = project)
    if request.method == "POST":
        form = EditRequirement(request.POST, instance= req)
        notify  = True
        if form.is_valid():
            form.save()
            message = "Requirement Edited."
        else:
            message = "Invalid Information"
    else:
        form = EditRequirement(instance=req)
    return render(request, "project/edit_requirement.html", locals())

@login_required(login_url="login.views.connect")
def delete_requirement(request,id):
    project = Project.objects.get(id = request.session['selected_project_id'] )
    req = get_object_or_404(Requirements,id = id, project = project)
    req.delete()
    return redirect("project.views.requirements");

def delete_project(request, id):
    pj = get_object_or_404(Project,id = id);
    pj.delete();
    return redirect("project.views.projects")
