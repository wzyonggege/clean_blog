from django import forms
from .models import Comment

class CommentForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    content = forms.CharField(
        label='Comment',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Content',
                                     'row': 3})
    )