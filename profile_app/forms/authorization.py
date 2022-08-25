from django import forms


class LoginForm(forms.Form):
    """Класс формы авторизации пользователя"""
    username = forms.CharField(max_length=128)                      # имя
    password = forms.CharField(widget=forms.PasswordInput())        # пароль