from django.shortcuts import render, redirect
from django.contrib import messages
from apps.recipes.models import *
from .models import User
import bcrypt
import datetime


def login_reg(request):
    return render(request, 'login_reg/register.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], birthday = request.POST['birthday'], email = request.POST['email'], password = pw_hash)
        request.session['userid'] = new_user.id
        username = new_user.first_name
        request.session['username'] = username
        return redirect("/user_profile")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        user = User.objects.filter(email = request.POST['login_email'])
        logged_user = user[0]
        request.session['userid'] = logged_user.id
        username = logged_user.first_name
        request.session['username'] = username
        return redirect('/user_profile')
        

def user_profile(request):
    if 'userid' in request.session:
        return render(request, 'login_reg/user_profile.html')
    else: 
        return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')

