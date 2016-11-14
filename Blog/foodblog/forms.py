from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text',)

class AuthForm(forms.ModelForm):

    class Meta:
        model = Auth
        fields = ('username','password','email','phone')
        widgets = {
        'password': forms.PasswordInput(),}

class Login(forms.ModelForm):

    class Meta:
        model = Auth
        fields = ('username','password')
        widgets = {
        'password': forms.PasswordInput(),}

