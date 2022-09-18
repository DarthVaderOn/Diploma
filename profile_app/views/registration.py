import os
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from profile_app.forms.registration import RegistrationForm
from profile_app.tasks import send_email_task
from django.contrib.auth import login


class RegistrationView(View):
    """Класс регистрации пользователя"""

    def get(self, request):
        """Представление формы"""
        if not request.user.is_authenticated:
            reg_form = RegistrationForm()
            contex = {
                'title': 'Registration',
                'reg_form': reg_form,
            }
            return render(request, 'registration_page.html', contex)
        else:
            return redirect('main_page')


    def post(self, request):
        """Сохранение формы"""
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user=reg_form.save()
            send_email_task()                             # sending letter
            send_mail('Welcome New User!',
                'Welcome to the sweetest site!\n\n\n- Post ads or browse the product catalog.\n- Add the products you like to your favorites, as well as leave your feedback about the product.\n\n\nWe are glad that you are with us!',
                str(os.getenv('EMAIL_HOST_USER')),        # Enter your email address
                [user.email])                             # Enter them email address
            login(request, user)
            return redirect('/')
        contex = {
            'title': 'Registration',
            'reg_form': reg_form,
        }
        return render(request, 'registration_page.html', contex)