from django import forms
from django.forms import ModelForm
from .models import User


class loginForm(forms.Form):
    name = forms.CharField(label='name')
    password = forms.CharField(label='password')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'age', 'gender', 'city']
