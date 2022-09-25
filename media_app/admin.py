from django.contrib import admin
from django.utils.safestring import mark_safe
from media_app.models import MediaFile
from catalog_app.models import Media


# Register your models here.


@admin.register(MediaFile)
class MessengerAdmin(admin.ModelAdmin):
    """Вывод полей медиафайлов в админке"""
    model = Media
    list_display = ('id', 'user', 'file', 'uploaded_at', 'preview')
    list_display_links = ('user', 'file',)
    list_filter = ('id', 'user',)
    ordering = ('-id',)
    readonly_fields = ('preview', 'uploaded_at')
    search_fields = ('user__username', 'file')


    def preview(self, obj):
        """Превью при нажатии на картинку"""
        if obj.file:
            return mark_safe(
                f'<a target=_blank href={obj.file.url}>'
                f'<img src={obj.file.url} width="100" height="100">'
                f'</a>'
            )