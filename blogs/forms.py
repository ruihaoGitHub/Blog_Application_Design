from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'header_image']
        labels = {'title': 'Title', 'text': 'Text', 'header_image': 'Header Image'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your post here...'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
