from django import forms
from .models import Post, Comment


class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentUploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
