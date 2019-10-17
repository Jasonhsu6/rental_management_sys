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
