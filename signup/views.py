<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group, Permission
from django.shortcuts import render, redirect

from signup.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            usergroup = form.cleaned_data.get('usertype')
            if usergroup == 'staff':
                group = Group.objects.get(name = 'staff')
                permission = Permission.objects.get(name = 'staff')
                user.groups.add(group)
                user.user_permissions.add(permission)
            elif usergroup == 'admin':
                group = Group.objects.get(name = 'moderator')
                permission = Permission.objects.get(name = 'moderator')
                user.groups.add(group)
                user.user_permissions.add(permission)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "Landing.html")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
=======
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/forms.html', {'form':form})
>>>>>>> 33c1eb452f33419e85fbd20e0b4ba4c94d27c6b2
