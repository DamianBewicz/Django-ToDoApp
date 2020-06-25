from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth import password_validation

polish_password_help_text = '''
</ul>
<li>Twoje hasło nie może być podobne do innych informacji.</li>
<li>Twoje hasło musi składać się z conajmniej 8 znaków.</li>
<li>Twoje hasło nie może być zbyt powszechne.</li>
<li>Twoje hasło nie może składać się w całości z cyfr.</li>
</ul>
'''

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Adres email")
    username = forms.CharField(max_length=255, required=True, label="Nazwa użytkownika")
    password1 = forms.CharField(
    label="Hasło",
    strip=False,
    widget=forms.PasswordInput,
    help_text=polish_password_help_text,
    )
    password2 = forms.CharField(
    label="Powtórz hasło",
    strip=False,
    widget=forms.PasswordInput,
    help_text="Wprowadź ponownie to samo hasło."
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]