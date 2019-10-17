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

            group = form.cleaned_data['usertype']
            group.user_set.add(user)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "Landing.html")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
# # =======
# from django.shortcuts import render,redirect
# from .forms import SignUpForm
# from django.contrib.auth.models import Group
#
# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             group = form.cleaned_data['group']
#             group.user_set.add(user)
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/forms.html', {'form':form})

