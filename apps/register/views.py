from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from apps.register.forms import UserForm


# Create your views here.

def signup(request):
    form = UserForm()
    if request.POST and form.is_valid():
        form = UserForm(request.POST or None)
        form.save()
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/post')
        else:
            loginError = 'Please enter corect Username or Password'
            message = {'loginError': loginError}
            return render(request, 'registration/signin.html', message)
    return render(request, 'registration/signin.html', locals())
