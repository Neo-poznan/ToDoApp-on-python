from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from users.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'id':'username-id-for-label',

    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'id':'password1-id-for-label',

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'id':'password2-id=for-label',

    }))    


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']




class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-input',
        'id':'username-id-for-label',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-input',
        'id':'password-id-for-label',
    }))


    class Meta:
        model = User
        fields = ['username', 'password']