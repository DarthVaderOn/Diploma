from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_app.models import User


class RegistrationForm(UserCreationForm):
    """Класс формы регистрации пользователя"""

    username = forms.CharField()
    email = forms.EmailInput()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Enter password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        """Вывод полей при регистрации"""
        model = User
        fields = ('username', 'email', 'password1', 'password2')