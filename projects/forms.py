from django import forms
from . import models

attrs = {'class' : 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields =['category', 'title', 'description']
        widgets = {
            'category': forms.Select(attrs),
            'title': forms.TextInput(attrs),
            'description': forms.Textarea(attrs),
        }



class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields =['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs),
            'title': forms.TextInput(attrs),
            'status': forms.Select(attrs),
        }

