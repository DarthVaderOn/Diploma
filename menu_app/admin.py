from django.contrib import admin
from menu_app.models import Menu, MenuItem


# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Вывод меню в админке"""
    model = Menu
    list_filter = ('menu_label',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Вывод полей меню в админке"""
    model = MenuItem
    list_display = ('menu', 'title', 'url', 'priority')
    list_display_links = ('menu', 'title', 'url',)
    list_editable = ('priority',)
    list_filter = ('menu', 'title', 'url', 'priority')
    search_fields = ('title', 'url', 'priority')