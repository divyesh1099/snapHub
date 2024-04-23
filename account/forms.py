from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_no = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile_no', 'email', 'password1', 'password2')
