from django.contrib import admin
from category_app.models import Tag


# Register your models here.


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    """Вывод полей тегов в админке"""
    list_display = ('id', 'title',)
    ordering = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)