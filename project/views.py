# Create your views here.
from django.shortcuts import render
from project.forms import NewProjectForm
from project.models import Project
from login.models import Profile
def project(request):
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