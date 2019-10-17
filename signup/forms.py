from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group,User


class UserRegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']
