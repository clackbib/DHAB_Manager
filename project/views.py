# Create your views here.
from django.shortcuts import render
from project.forms import NewProjectForm
from project.models import Project
from login.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

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
            message = 'Project Successfully Created!'
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
    request.session['selected_project'] = request.POST['project']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),locals())