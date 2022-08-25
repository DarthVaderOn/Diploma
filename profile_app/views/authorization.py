from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from profile_app.forms.authorization import LoginForm


class Authorization(View):
    """Класс авторизации пользователя"""

    @staticmethod
    def get(request):
        """Представление формы"""
        if not request.user.is_authenticated:
            form = LoginForm()
            contex = {
                'auth_form': form,
            }
            return render(request, 'authorization_page.html', contex)
        else:
            return redirect('main_page')


    @staticmethod
    def post(request):
        """Сохранение формы"""

        form = LoginForm(request.POST)
        error = False

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user is not None:
                auth.login(request, user)

                next_page =request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        contex = {
            'title': 'Authorization',
            'auth_form': form,
            'error': error,
        }
        return render(request, 'authorization_page.html', contex)