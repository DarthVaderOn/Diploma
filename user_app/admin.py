from django.contrib import admin
from profile_app.models import Profile
from .models import User
from django.contrib.auth.admin import UserAdmin as UserAdminBase


# Register your models here.


class ProfileInline(admin.StackedInline):
    """Вывод полей профайла в админке"""
    model = Profile


@admin.register(User)
class UserAdmin(UserAdminBase):
    """Вывод User (и Profile) и настойки админки"""
    inlines = (
        ProfileInline,
    )

    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('id', 'username', 'email',)
    list_filter = ('username', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)