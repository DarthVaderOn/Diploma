from django.contrib import admin
from menu_app.models import Menu, MenuItem


# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Вывод меню в админке"""
    model = Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Вывод полей меню в админке"""
    model = MenuItem