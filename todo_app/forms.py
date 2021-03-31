from django import forms
from .models import Todo, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# for add delete edit
class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user']


# for signup
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2'
                  ]


# for login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_image',]


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
