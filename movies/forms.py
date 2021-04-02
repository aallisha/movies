from .models import MovieComment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Defines what values our comment form will have
    """
    class Meta:
        model = MovieComment
        fields = ('name', 'email', 'body', 'movie')
