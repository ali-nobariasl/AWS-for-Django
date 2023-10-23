from django import forms
#for registeration 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# for login
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput , TextInput

from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = {'username', 'password1', 'password2','email'}



class LoginUserForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



class UpdateUserForm(forms.ModelForm):

    password = None
    class Meta:
        model =User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']




class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields =['profile_pic']