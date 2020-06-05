from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth import password_validation

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Adres email")
    username = forms.CharField(max_length=255, required=True, label="Nazwa użytkownika")
    password1 = forms.CharField(
    label="Hasło",
    strip=False,
    widget=forms.PasswordInput,
    help_text=password_validation.password_validators_help_text_html(),
)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]