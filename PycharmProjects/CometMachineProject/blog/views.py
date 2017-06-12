from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from blog.forms import SignUpForm, LogInForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        registration = SignUpForm(request.POST)
        if registration.is_valid():
            registration.save()
            username = registration.cleaned_data.get('username')
            raw_password = registration.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mainpage')
    else:
        registration = SignUpForm()

    if request.method == 'POST':
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            login_form.save()
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainpage')
            else:
                return redirect('http://facebook.com')

    else:
        login_form = LogInForm()

    return render(request, 'homepage.html', {'registration': registration, 'login':login_form})


def mainpage(request):
    return render(request, 'mainpage.html')
