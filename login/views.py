# Create your views here.
from django.shortcuts import render
from login.forms import Registration

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
    else:
        form = Registration()
    return render(request, 'register.html', locals())