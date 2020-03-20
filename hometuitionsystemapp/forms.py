from django import forms
from .models import *


class HomeTuitionSystemCreateForm(forms.ModelForm):
    class Meta:
        model = HomeTuitionSystem
        fields = "__all__"
