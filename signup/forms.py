from django import forms
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=False, help_text='Optional')
    usertype = forms.ChoiceField(choices=[("staff", "staff"), ("admin", "admin")])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2', 'usertype')
=======
from django.contrib.auth.models import Group,User


class UserRegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']
>>>>>>> 33c1eb452f33419e85fbd20e0b4ba4c94d27c6b2
