from django import forms


class LoginForm(forms.Form):
    """Класс формы авторизации пользователя"""
    username = forms.CharField(min_length=3, max_length=128, widget=forms.PasswordInput(),)     # имя
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())                      # пароль