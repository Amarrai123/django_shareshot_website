from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("username","first_name","email")
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('password didnot match')
        return cd['password']   

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','email','last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('date_of_birth','photo')
