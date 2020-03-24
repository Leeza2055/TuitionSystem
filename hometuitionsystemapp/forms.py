from django import forms
from .models import *


class HomeTuitionSystemCreateForm(forms.ModelForm):
    class Meta:
        model = HomeTuitionSystem
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username..",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter your password ..",
        "class": "form-control",
    }))
