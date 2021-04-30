from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#from .forms import *
#from django.forms import modelformset_factory, inlineformset_factory
from django.core.files.storage import FileSystemStorage
from crispy_forms.helper import FormHelper

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_dashboard')
        else:
            messages.info(request, 'Username atau Password tidak valid!')
    context = {}
    return render(request, 'manajemen_kontrak/login_page.html', context)

def home_dashboard(request):
    return HttpResponse('Laman dashboard')
