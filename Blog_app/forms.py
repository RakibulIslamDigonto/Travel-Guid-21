from django.core import validators
from django import forms
from django.db.models import fields
from .models import User, Comment


class UserRegistation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }


class CommForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

