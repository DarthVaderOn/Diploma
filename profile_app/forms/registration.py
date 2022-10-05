from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_app.models import User


class RegistrationForm(UserCreationForm):
    """Класс формы регистрации пользователя"""

    username = forms.CharField(min_length=3, widget=forms.PasswordInput())
    email = forms.EmailInput()
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Enter password')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        """Вывод полей при регистрации"""
        model = User
        fields = ('username', 'email', 'password1', 'password2')