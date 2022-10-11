from django.contrib.auth.models import User
from django import forms
from profile_app.models import Profile


class UpdateUserForm(forms.ModelForm):
    """Класс формы обновления данных User"""

    class Meta:
        model = User
        fields = ["last_name", "first_name", "email",]


class UpdateProForm(forms.ModelForm):
    """Класс формы обновления данных Profile"""

    class Meta:
        model = Profile
        fields = ["avatar", "phone", "about",]