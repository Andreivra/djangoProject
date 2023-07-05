from django import forms
from django.forms import TextInput, EmailInput, Select, RadioSelect

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your teaching course', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email',  'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-select'}),

        }


class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'email', 'department', 'profile', 'file']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'course': TextInput(attrs={'placeholder': 'Please enter your teaching course', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email',  'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-select'}),

        }
