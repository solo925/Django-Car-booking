from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone=forms.CharField(max_length=13)
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label="password",widget=forms.PasswordInput())
