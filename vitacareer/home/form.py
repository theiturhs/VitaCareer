from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BasicUserDetails

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'contact', 'role', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
class BasicUserDetailsForm(forms.ModelForm):
    class Meta:
        model = BasicUserDetails
        fields = ['age', 'looking_for', 'field', 'bio', 'organization', 'job_role', 'experience']
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'looking_for': forms.Select(attrs={'class': 'form-control'}),
            'field': forms.Select(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'job_role': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
        }