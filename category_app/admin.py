from django.contrib import admin
from category_app.models import Tag


# Register your models here.


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    """Вывод полей категорий и настройки админки"""
    list_display = ('id', 'title',)
    list_filter = ('id', 'title',)
    ordering = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)