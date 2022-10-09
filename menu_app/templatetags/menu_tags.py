from django import template
from django.urls import reverse
from menu_app.models import Menu


register = template.Library()


@register.inclusion_tag('menu.html')
def main_menu():
    menu = Menu.objects.get(menu_label='main_menu')
    return {'menu': menu.links.order_by('priority').all()}


@register.inclusion_tag('menu.html', takes_context=True)
def user_menu(context):
    if context.request.user.is_authenticated:
        menu = [
            {
                'title': 'Logout',
                'url': reverse('logout_page'),
            },
        ]
    else:
        menu = [
            {
                'title': 'Sign In',
                'url': reverse('auth_page'),

            },
            {
                'title': 'Sign Up',
                'url': reverse('reg_page'),
            },
        ]
    return {'menu': menu}