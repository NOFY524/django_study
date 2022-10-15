from django import forms
from .models import Post, Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image')
