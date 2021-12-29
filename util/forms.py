from django import forms
from django.forms import ModelForm
from .models import User
from .models import Diagnosis


class loginForm(forms.Form):
    name = forms.CharField(label='name')
    password = forms.CharField(label='password')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'age', 'gender', 'city']


class DiagnosticsForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['name', 'doctor', 'hospital', 'prescription','patient']
