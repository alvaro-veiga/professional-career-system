from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from .models import *
from django.http import HttpResponse
from .forms.candidate import *
from django.contrib import messages
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
#from weasyprint import HTML

def profile(request):
    return render(request, 'profile.html')

def oportunity(request):
    return render(request, 'oportunity.html')

def oportunity_detail(request):
    return render(request, 'oportunity_detail.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('oportunity')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Erro ao enviar o formulário.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Sua conta foi criada com sucesso! Você pode fazer login agora.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao enviar o formulário.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

"""def generatePDF(request, *args, **kwargs):
    template = get_template('pdf/profile_pdf.html')

    profile = {
        'name': '...',
        'date_of_birth': '...',
        'phone': '...',
        'address': '...',
        'about': '...',
        'education': '...',
        'experience': '...',
        'skills': '...',
    }

    html_template = template.render(profile)
    html = HTML(string=html_template, base_url=request.build_absolute_uri())
    pdf = html.write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')"""