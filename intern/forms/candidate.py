from ..models import UserAutentication
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserAutentication
        fields = ['email', 'password']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Campo obrigatório. Informe um e-mail válido.')
    username = forms.CharField(max_length=30, help_text='Campo obrigatório. Máximo 30 caracteres.')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = UserAutentication
        fields = ('email', 'username', 'password1', 'password2')