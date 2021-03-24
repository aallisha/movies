from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from movie.models import Review,RATE_CHOICES
class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')


