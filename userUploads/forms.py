from django import forms

from .models import UserUploads

class UserForm(forms.ModelForm):
    class Meta:
        model = UserUploads
        fields = [
            'Job_Description',
            'Resume'
        ]