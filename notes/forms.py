from django.forms import ModelForm
from django import forms
from .models import Note

class createForm(ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Note
        fields = ['title', 'description']