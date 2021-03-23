from .models import MovieComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('name', 'email', 'body')
