# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from login.forms import Registration, ConnectionForm
from login.models import Profile


def register(request):
    error = False
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email)
            user2 = User.objects.filter(username=username)

            if user:
                message = "Email address already in use"
                error = True
            elif user2:
                message = "Username already in use"
                error = True
            else:
                user3 = User.objects.create_user(username, email, password)
                Profile(user=user3).save(); #Profile Created based on User.
                return redirect("login.views.register")
        else:
            error = True
            message = 'Form invalid'
    else:
        form = Registration()
    return render(request, 'register.html', locals())


def connect(request):
    notify = False
    message = ""
    request.session['selected_project'] = None
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            message = "valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("project.views.projects")
            else:
                notify = True
                message = "Invalid credentials"

        else:
            message = "Fields incomplete."
            notify = True
    else:
        form = ConnectionForm()
    return render(request, 'login.html', locals())


@login_required(login_url="login.views.connect")
def disconnect(request):
    logout(request)
    return redirect(reverse("login.views.connect"))


