from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm, PostForm
from .models import User, Post
from django import forms
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            if password2 != password:
                raise forms.ValidationError("The password does not match")
            else:
                user = User()
                user.username = username
                user.password = password
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                login(request, user)

    else:
        form = UserForm()

    return render(request, "register.html", {'UserForm': form})


def mainpage(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            post_content = form.cleaned_data['post_content']
            post_title = form.cleaned_data['post_title']
            post = Post()
            post.post_title = post_title
            post.post_content = post_content
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    return render(request, "mainpage.html", {'PostForm': form})
