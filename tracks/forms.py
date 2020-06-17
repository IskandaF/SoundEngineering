from django import forms
from .models import Track,Project
from django.forms import ModelForm
from django.forms.widgets import NumberInput,RadioSelect

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=[
            "name",
        ]

class AddTracksForm(forms.ModelForm):
    class Meta:
        model=Track
        fields = '__all__'
        widgets={
            
            "project":forms.HiddenInput(),
        }
